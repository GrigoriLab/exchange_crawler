from django.contrib import admin

from apps.quote.models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("from_currency_code", "from_currency_name", "to_currency_code", "to_currency_name", "exchange_rate", "last_refreshed", "time_zone", "bid_price", "ask_price")
    search_fields = ("from_currency_code", "from_currency_name", "to_currency_code", "to_currency_name", "exchange_rate", "last_refreshed", "time_zone", "bid_price", "ask_price")
    readonly_fields = ("from_currency_code", "from_currency_name", "to_currency_code", "to_currency_name", "exchange_rate", "last_refreshed", "time_zone", "bid_price", "ask_price")
    list_filter = ("from_currency_code", "to_currency_code", )
