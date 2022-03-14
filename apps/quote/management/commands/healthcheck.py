from django.core.management.base import BaseCommand

from apps.quote.tasks import crawler
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Check DB connection"

    def handle(self, *args, **options):
        db_conn = connections['default']
        try:
            c = db_conn.cursor()
        except OperationalError:
            print("Not connected")
            exit(1)
        else:
            print("Connected")
            exit(0)
