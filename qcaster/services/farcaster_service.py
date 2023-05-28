import requests
import logging
from flask import current_app as app

class FarcasterService:

    def __init__(self):
        self.headers = {
            'Authorization': app.config["FARCASTER_AUTHORIZATION_HEADER"],
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def create_post(self, text):
        try:
            response = requests.post(
                'https://api.warpcast.com/v2/casts',
                headers=self.headers,
                data={'text': text}
            )

            if response.status_code == 200:
                logging.info(f"Farcaster post created successfully.")
                return True
            else:
                logging.error(f"Error occurred while creating Farcaster post: {response.content}")
                return False
        except Exception as e:
            logging.error(f"Error occurred while creating Farcaster post: {e}")
            return False

