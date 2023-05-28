import tweepy
import logging
from flask import current_app as app

class TweetService:

    def __init__(self):
        self.client = tweepy.Client(
            consumer_key=app.config["TWITTER_CONSUMER_KEY"],
            consumer_secret=app.config["TWITTER_CONSUMER_SECRET"],
            access_token=app.config["TWITTER_ACCESS_TOKEN"],
            access_token_secret=app.config["TWITTER_ACCESS_TOKEN_SECRET"]
        )

    def post_tweet(self, text):
        try:
            response = self.client.create_tweet(text=text)
            logging.info(f"Posted tweet: https://twitter.com/user/status/{response.data['id']}")
            return True
        except Exception as e:
            logging.error(f"Error occurred while posting tweet: {e}")
            return False

