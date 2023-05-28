from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280), nullable=False)
    posted = db.Column(db.Boolean, default=False)

