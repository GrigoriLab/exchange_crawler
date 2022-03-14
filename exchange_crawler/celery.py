import os
from datetime import timedelta

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange_crawler.settings')
app = Celery('exchange_crawler')

app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.beat_schedule = {
#     "exchange_crawler_each_hour": {
#         "task": "apps.quote.tasks.crawler",
#         "schedule": timedelta(hours=1),
#     },
# }
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
