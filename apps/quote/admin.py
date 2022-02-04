from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.quote.models import Quote
from apps.quote.tasks import crawler


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("from_currency_code", "from_currency_name", "to_currency_code", "to_currency_name", "exchange_rate", "last_refreshed", "time_zone", "bid_price", "ask_price")
    search_fields = ("from_currency_code", "from_currency_name", "to_currency_code", "to_currency_name", "exchange_rate", "last_refreshed", "time_zone", "bid_price", "ask_price")
    readonly_fields = ("from_currency_code", "from_currency_name", "to_currency_code", "to_currency_name", "exchange_rate", "last_refreshed", "time_zone", "bid_price", "ask_price")
    list_filter = ("from_currency_code", "to_currency_code", )

    def get_urls(self):
        urls = super().get_urls()

        extra = [
            url(
                r"fetch_data/$",
                self.admin_site.admin_view(self.fetch_data),
                name="quote_quote_fetch_data",
            ),
        ]
        return extra + urls

    def fetch_data(self, request):
        crawler()
        return HttpResponseRedirect(reverse("admin:quote_quote_changelist"))
