import requests

X_COINAPI_KEY = ''
API_URL = ''


def setup(api_url, api_key):
    global X_COINAPI_KEY
    global API_URL
    X_COINAPI_KEY = api_key
    API_URL = api_url


def coinapi_request(endpoint):
    api_headers = {'X-CoinAPI-Key': X_COINAPI_KEY}
    response = requests.get(API_URL + endpoint, headers=api_headers).json()
    return response


def get_exchange_rate(currency_name):
    endpoint = f'exchangerate/{currency_name}/USD'
    response = coinapi_request(endpoint)
    return response


def get_exchange_rate_history(currency_name, start_date):
    endpoint = f'exchangerate/{currency_name}/USD/history?period_id=1DAY&time_start={start_date}T00:00:00'
    response = coinapi_request(endpoint)
    return response
