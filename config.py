import os
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

class Config():
    DEBUG = True
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'. \
        format(os.environ.get('SQLALCHEMY_USER'),
               os.environ.get('SQLALCHEMY_PASSWORD'),
               os.environ.get('SQLALCHEMY_HOST'),
               os.environ.get('SQLALCHEMY_PORT'),
               os.environ.get('SQLALCHEMY_DB'))
    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_PASS = os.environ.get('REDIS_PASS')
    CELERY_TIMEZONE = 'Europe/Istanbul'
