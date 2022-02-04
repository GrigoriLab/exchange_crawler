from unittest.mock import patch

from apps.api.tests.base import BaseTestCase
from django.test import override_settings


class QuotesTestCase(BaseTestCase):
    fixtures = [
        "quote.json",
        "user.json"
    ]

    def test_get_quotes(self):
        self.api_client.login("admin", "admin")
        resp = self.api_client.get("quotes/")
        expected_quote = {
            "id": 1,
            "from_currency_code": "BTC",
            "from_currency_name": "Bitcoin",
            "to_currency_code": "USD",
            "to_currency_name": "United States Dollar",
            "exchange_rate": "37931.35000000",
            "last_refreshed": "2022-02-04T11:45:01Z",
            "time_zone": "UTC",
            "bid_price": "37931.35000000",
            "ask_price": "37931.36000000"
        }
        self.assertDictEqual(expected_quote, resp.json[0])

    def test_quotes_unauthorized(self):
        resp = self.api_client.get("quotes/")
        self.assertEqual(resp.status_code, 401)
        resp = self.api_client.post("quotes/", data={})
        self.assertEqual(resp.status_code, 401)

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    @patch("apps.quote.tasks.ForeignExchange.get_currency_exchange_rate")
    @patch("apps.quote.tasks.Quote.objects.create")
    def test_post_quotes(self, m_quote_create, m_api):
        expected_data = {
            '1. From_Currency Code': 'BTC',
            '2. From_Currency Name': 'Bitcoin',
            '3. To_Currency Code': 'USD',
            '4. To_Currency Name': 'United States Dollar',
            '5. Exchange Rate': '37931.35000000',
            '6. Last Refreshed': '2022-02-04T11:45:01Z',
            '7. Time Zone': 'UTC',
            '8. Bid Price': '37931.35000000',
            '9. Ask Price': '37931.36000000'
        }
        expected_kwargs = {
            "from_currency_code": expected_data["1. From_Currency Code"],
            "from_currency_name": expected_data["2. From_Currency Name"],
            "to_currency_code": expected_data["3. To_Currency Code"],
            "to_currency_name": expected_data["4. To_Currency Name"],
            "exchange_rate": expected_data["5. Exchange Rate"],
            "last_refreshed": expected_data["6. Last Refreshed"],
            "time_zone": expected_data["7. Time Zone"],
            "bid_price": expected_data["8. Bid Price"],
            "ask_price": expected_data["9. Ask Price"]
        }

        m_api.return_value = expected_data, "doesn't matter"
        self.api_client.login("admin", "admin")
        resp = self.api_client.post("quotes/", data={})

        expected_resp = {"info": "crawler manually triggered!"}
        self.assertDictEqual(resp.json, expected_resp)
        self.assertEqual(resp.status_code, 201)
        m_quote_create.assert_called_with(**expected_kwargs)
