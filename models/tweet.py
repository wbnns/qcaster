from tweet_scheduler import db  # Import the db object here or in specific functions/methods
from .database import db

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280), nullable=False)
    # ...

