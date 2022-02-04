import logging

from alpha_vantage.foreignexchange import ForeignExchange

from apps.quote.models import Quote
from exchange_crawler.celery import app

logger = logging.getLogger(__name__)


@app.task(bind=True)
def crawler(self):
    cc = ForeignExchange()
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',
                                            to_currency='USD')
    quote = Quote.objects.create(
        from_currency_code=data["1. From_Currency Code"],
        from_currency_name=data["2. From_Currency Name"],
        to_currency_code=data["3. To_Currency Code"],
        to_currency_name=data["4. To_Currency Name"],
        exchange_rate=data["5. Exchange Rate"],
        last_refreshed=data["6. Last Refreshed"],
        time_zone=data["7. Time Zone"],
        bid_price=data["8. Bid Price"],
        ask_price=data["9. Ask Price"],
    )
    logger.info('Crawler request: {0!r}'.format(self.request))
    logger.info(f'Got Quote: {quote}')
