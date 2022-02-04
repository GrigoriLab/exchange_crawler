from django.core.management.base import BaseCommand

from apps.quote.tasks import crawler


class Command(BaseCommand):
    help = "Fetch data from alphavantage and store it in the DB."

    def handle(self, *args, **options):
        crawler()
