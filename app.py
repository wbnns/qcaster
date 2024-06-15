import os
import random
import threading
import time
from datetime import datetime, timedelta

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import tweepy
import requests
import json
from dotenv import load_dotenv
import click
from flask.cli import with_appcontext
from flask_migrate import Migrate

# Load environment variables from the .env file
load_dotenv()

# Get keys from environment variables
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
farcaster_auth_header = os.getenv("FARCASTER_AUTHORIZATION_HEADER")

# Initialize Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tweets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Authenticate as a user
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280), nullable=False)
    scheduled_time = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

@app.route('/')
def home():
    tweets = Tweet.query.order_by(Tweet.scheduled_time).all()
    return render_template('index.html', tweets=tweets)

@app.route('/add', methods=['POST'])
def add():
    text = request.form['text']
    now = datetime.utcnow()

    # Get the latest scheduled time from the database
    latest_tweet = Tweet.query.order_by(Tweet.scheduled_time.desc()).first()

    # Calculate the scheduled time for the new tweet
    if latest_tweet:
        min_scheduled_time = latest_tweet.scheduled_time + timedelta(minutes=12)
    else:
        min_scheduled_time = now + timedelta(minutes=12)

    max_scheduled_time = min_scheduled_time + timedelta(minutes=12)
    scheduled_time = random_datetime(min_scheduled_time, max_scheduled_time)

    tweet = Tweet(text=text, scheduled_time=scheduled_time)
    db.session.add(tweet)
    db.session.commit()
    return redirect(url_for('home'))

# Helper function to generate a random datetime within a given range
def random_datetime(start, end):
    delta = end - start
    random_seconds = random.randrange(int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

@app.route('/delete/<int:id>')
def delete(id):
    tweet = Tweet.query.get(id)
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

@app.route('/post_now/<int:id>')
def post_now(id):
    tweet = Tweet.query.get(id)
    job(tweet.text)
    db.session.delete(tweet)
    db.session.commit()
    return redirect(url_for('home'))

def job(text):
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

def run_scheduler():
    while True:
        with app.app_context():
            try:
                now = datetime.utcnow()
                tweet = Tweet.query.filter(Tweet.scheduled_time <= now + timedelta(minutes=3)).first()
                if tweet:
                    job(tweet.text)
                    db.session.delete(tweet)
                    db.session.commit()
            except Exception as e:
                app.logger.exception("Error in scheduler: %s", str(e))
                db.session.rollback()
            finally:
                db.session.remove()  # Remove the database session to release the connection

        time.sleep(60)

@app.cli.command('run_scheduler')
def run_scheduler_command():
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()

if __name__ == '__main__':
    app.run(debug=True)
