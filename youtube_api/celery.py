import os
from celery import Celery
from celery.schedules import crontab

from django.conf import settings
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_api.settings')
 
app = Celery('youtube_api')
app.config_from_object('django.conf:settings', namespace="CELERY")
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

CELERY_BEAT_SCHEDULE = {
    'fetch-and-update-database': {
        'task': 'api.cron.fetch_and_update_db',
        'schedule': crontab(minute='*/{}'.format(settings.CRON_RUN_FREQENCY_MINS)),
    },
}