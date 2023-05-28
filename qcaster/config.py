import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Config:
    # Get keys from environment variables
    BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
    CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
    ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    FARCASTER_AUTH_HEADER = os.getenv("FARCASTER_AUTHORIZATION_HEADER")
    POST_TO_TWITTER = os.getenv("POST_TO_TWITTER") == "True"
    POST_TO_FARCASTER = os.getenv("POST_TO_FARCASTER") == "True"
    DATABASE_URL = os.getenv("DATABASE_URL")

