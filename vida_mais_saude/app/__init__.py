from flask import Flask

from config import AppConfig

def create_app(config=AppConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    return app
