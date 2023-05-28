from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler
import os
import tweepy
import requests
import json
import logging

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Get keys from environment variables
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
farcaster_auth_header = os.getenv("FARCASTER_AUTHORIZATION_HEADER")

# Create a logger
logging.basicConfig(filename='errors.log', level=logging.ERROR)

# Authenticate as a user
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tweets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280), nullable=False)
    posted = db.Column(db.Boolean, default=False)

@app.route('/')
def home():
    tweets = Tweet.query.filter_by(posted=False).all()
    return render_template('index.html', tweets=tweets)

@app.route('/add', methods=['POST'])
def add():
    text = request.form.get('text')
    tweet = Tweet(text=text)
    db.session.add(tweet)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    tweet = Tweet.query.get(id)
    if tweet:
        db.session.delete(tweet)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    tweet = Tweet.query.get(id)
    if request.method == 'POST':
        tweet.text = request.form.get('text')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', tweet=tweet)

@app.route('/post/<int:id>')
def post(id):
    tweet = Tweet.query.get(id)
    if tweet:
        job(tweet.text, tweet.id)
        tweet.posted = True
        db.session.commit()
    return redirect(url_for('home'))

def job(text=None, tweet_id=None):
    try:
        if text is None and tweet_id is None:
            # If no parameters were given, get the oldest unposted tweet
            tweet = Tweet.query.filter_by(posted=False).first()
            if tweet is not None:
                text = tweet.text
                tweet_id = tweet.id

        if text is not None:
            # Create a tweet
            response = client.create_tweet(text=text)
            print(f"https://twitter.com/user/status/{response.data['id']}")

            # Post to Farcaster
            farcaster_response = requests.post(
                'https://api.warpcast.com/v2/casts',
                headers={
                    'Authorization': farcaster_auth_header,
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                data=json.dumps({'text': text})
            )
            print(f"Farcaster post response status: {farcaster_response.status_code}")

            if tweet_id is not None:
                # If a tweet id was given, mark the tweet as posted
                tweet = Tweet.query.get(tweet_id)
                tweet.posted = True
                db.session.commit()

    except Exception as e:
        logging.error(f"Error occurred: {e}")

# Schedule job for 9AM and 12AM
scheduler = BackgroundScheduler()
scheduler.add_job(job, 'cron', hour='9,0')
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)

