from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feedreader.settings')

app = Celery('feedreader')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# To run Celery beat --> celery -A feedreader beat
# To run worker --> celery -A feedreader worker -l info