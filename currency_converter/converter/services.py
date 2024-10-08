import requests

from currency_converter.currency_converter.settings import API_KEY


def get_exchange_rate(base_currency, target_currency):
    API_URL = "https://openexchangerates.org/api/latest.json"

    response = requests.get(API_URL, params={
        'app_id': API_KEY,
        'base': base_currency,
        'symbols': target_currency,
    })

    data = response.json()
    rate = data['rates'].get(target_currency)
    return rate