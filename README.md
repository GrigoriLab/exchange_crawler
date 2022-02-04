## Exchange Crawler

This is a small app which fetches data from alphavantage API each hour and stores it in the DB.
It also provides an API to manually trigger the fetch job and get stored data.

### Run
Before running the app you will need to configure the environment by creating `.env` file with following content.
```bash
RABBITMQ_USER=guest
RABBITMQ_PASS=guest
RABBITMQ_HOST=rabbitmq
ALPHAVANTAGE_API_KEY=EQCMXBI1WI98VIKX
POSTGRES_USER=postgres
POSTGRES_PASS=postgres
POSTGRES_HOST=postgres
POSTGRES_DB=postgres
DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASS}@${POSTGRES_HOST}:5432/${POSTGRES_DB}

```

To run the project please execute following command:
```bash
docker-compose up
```

Now you should be able to go to [this](http://localhost:8000/admin/) url and sign in with following credentials.
```bash
username=admin
password=admin
```

To run the tests please execute following command:
```bash
docker-compose exec runserver python manage.py test -v 2
```

### API
To test the api you can send the requests manually from command line.

* Authenticate
    ```bash
    curl --location --request POST 'http://localhost:8000/api/v1/auth/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "username": "admin",
        "password": "admin"
    }'
    ```
    You will get the response with token
    ```json
    {"token":"2693bcf93c4d9e767a97c30605fa3131745bb65c"}
    ```

* Make a request
    
    Now you need to use this token in your requests' header like this:
    ```bash
    curl --location --request GET 'http://localhost:8000/api/v1/quotes/' \
    --header 'Authorization: Token 2693bcf93c4d9e767a97c30605fa3131745bb65c'
    ```
    And the response should be something like this.
    ```json
    [
      {
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
    ]
    ```
    To trigger fetch job manually you can use either `POST` method on the same endpoint or `FETCH DATA` button in django admin.

    ```bash
    curl --location --request POST 'http://localhost:8000/api/v1/quotes/' \
    --header 'Authorization: Token 2693bcf93c4d9e767a97c30605fa3131745bb65c'
    ```
