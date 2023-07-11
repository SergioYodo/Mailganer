import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core', broker=settings.CELERY_BROKER_URL)

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'send_email_every_minute': {
        'task': 'emails.tasks.send_email',
        'schedule': crontab(),
    },
    'get_log_every_five_minute': {
        'task': 'emails.tasks.get_logs',
        'schedule': crontab(minute=5),
    }
}
