from flask import Flask

from config import AppConfig
from app.database import db

def create_app(config=AppConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    return app
