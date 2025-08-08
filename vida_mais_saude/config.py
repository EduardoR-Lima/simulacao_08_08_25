import os

from dotenv import load_dotenv

_cur_dir = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(_cur_dir, '.env'))

class AppConfig:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
