from flask import Flask, request, render_template, redirect, url_for
from models import db, Tweet
from app import app

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
        # Post the tweet with the job function from your script
        job(tweet.text)
        tweet.posted = True
        db.session.commit()
    return redirect(url_for('home'))

