"""Default configuration

Use env var to override
"""

import os

from celery.schedules import crontab
from dotenv import load_dotenv


class Config(object):
    """
    Default Configuration
    """

    load_dotenv()
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    ENV = os.getenv("FLASK_ENV")
    DEBUG = ENV == "development"
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY = {
        "broker_url": os.getenv("CELERY_BROKER_URL"),
        "result_backend": os.getenv("CELERY_RESULT_BACKEND_URL"),
    }
    CELERYBEAT_SCHEDULE = {
        "get_latest_price": {
            "task": ".get_latest_price",
            "schedule": crontab(second='*/30', hour='9-17'),
        },
    }
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    REDIS_URL = os.getenv("REDIS_URL")

    INSTALLED_RESOURCES = [

    ]
    BROKER_URL = os.getenv("CELERY_BROKER_URL")
    RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")
    ACCEPT_CONTENT = ["json"]
    TASK_SERIALIZER = os.getenv("CELERY_TASK_SERIALIZER")
    RESULT_SERIALIZER = os.getenv("CELERY_RESULT_SERIALIZER")
    REDIS_MAX_CONNECTIONS = int(os.getenv("CELERY_REDIS_MAX_CONNECTIONS"))

    # To enable flask to catch package exceptions
    PROPAGATE_EXCEPTIONS = True
