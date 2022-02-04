import logging

from exchange_crawler.celery import app

logger = logging.getLogger(__name__)


@app.task(bind=True)
def debug_task(self):
    print("running debug_task")
