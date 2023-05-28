from flask import Flask
from . import views

def create_app():
    app = Flask(__name__)

    # Register blueprints or initialize app configurations here if any

    return app

