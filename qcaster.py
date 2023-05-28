import tweepy
import time
from dotenv import load_dotenv
import os
import logging
import schedule
import requests
import json

# Load environment variables from the .env file
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

def job(text):
    try:
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
    except Exception as e:
        logging.error(f"Error occurred: {e}")

# Schedule job for 9AM and 12AM
schedule.every().day.at("09:00").do(job, "Gm")
schedule.every().day.at("00:00").do(job, "Gn") # Changed "GN" to "Gn"

tweet_posted = False

while True:
    try:
        # Open the file and read the tweet
        with open('queue.txt', 'r') as file:
            lines = file.readlines()

        if lines:
            tweet_text = lines[0].strip()

            # Run the job with the read tweet text
            job(tweet_text)

            # Remove the tweeted line from the file
            with open('queue.txt', 'w') as file:
                file.writelines(lines[1:])

            tweet_posted = True
            # Wait for 72 minutes before posting the next tweet
            time.sleep(72 * 60)

        else:
            if tweet_posted:
                print('All tweets have been posted. Please add more tweets.')
                tweet_posted = False
            # Wait for 1 minute before checking the file again
            time.sleep(60)

    except Exception as e:
        logging.error(f"Error occurred: {e}")

    # Run pending schedule tasks
    schedule.run_pending()
    time.sleep(1)

