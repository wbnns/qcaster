from flask import render_template, request, redirect, url_for
from . import app
from .models import db, Tweet

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tweet_text = request.form['tweet_text']
        new_tweet = Tweet(text=tweet_text)
        db.session.add(new_tweet)
        db.session.commit()
        return redirect(url_for('home'))
    tweets = Tweet.query.all()
    return render_template('home.html', tweets=tweets)

