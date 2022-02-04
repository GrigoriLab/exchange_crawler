from django.db import models


class Quote(models.Model):
    from_currency_code = models.CharField(max_length=128)
    from_currency_name = models.CharField(max_length=128)
    to_currency_code = models.CharField(max_length=128)
    to_currency_name = models.CharField(max_length=128)
    exchange_rate = models.CharField(max_length=128)
    last_refreshed = models.DateTimeField()
    time_zone = models.CharField(max_length=128)
    bid_price = models.CharField(max_length=128)
    ask_price = models.CharField(max_length=128)

    class Meta(object):
        ordering = ['-last_refreshed', 'from_currency_code']

    def __str__(self):
        return f"{self.from_currency_code}/{self.to_currency_code}"
