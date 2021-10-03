from celery import Celery
from celery.schedules import crontab

from config import Config

celery = Celery(__name__)
celery.conf.broker_url = 'redis://{0}:6379/0'.format(Config.REDIS_HOST)
celery.conf.result_backend = 'redis://{0}:6379/0'.format(Config.REDIS_HOST)
celery.conf.add_defaults(Config)

celery.conf.beat_schedule = {
    'check_expire_date': {
        'task': 'src.celery.tasks.check_expire_date',
        'schedule': crontab(minute=0, hour='*/23'),
    },
}