from unittest.mock import patch
from adapters.coinapi_adapter import setup, coinapi_request, get_exchange_rate, get_exchange_rate_history
import adapters.coinapi_adapter
import unittest


class CoinApiTest_setup(unittest.TestCase):
    def test_should_verify_global_variables_are_correctly_set_based_on_input(self):
        # prepare

        # run
        setup('https://test_url', 'test_key')

        # assert
        self.assertEqual(adapters.coinapi_adapter.API_URL, 'https://test_url')
        self.assertEqual(adapters.coinapi_adapter.X_COINAPI_KEY, 'test_key')


class CoinApiTest_coinapi_request(unittest.TestCase):
    @patch('requests.get')
    def test_should_call_coinapi_and_return_correct_result(self, mock_get):
        # prepare
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'btc': 20000}

        # run
        result = coinapi_request('test_endpoint')

        # assert
        self.assertEqual(result, {'btc': 20000})

    @patch('requests.get')
    def test_should_check_api_key_existence_in_the_headers_with_correct_endpoint(self, mock_get):
        # prepare
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'btc': 20000}

        # run
        result = coinapi_request('test_endpoint')

        # assert
        mock_get.assert_called_with(
            'test_endpoint', headers={'X-CoinAPI-Key': ''})


class CoinApiTest_get_exchange_rate(unittest.TestCase):
    @patch('adapters.coinapi_adapter.coinapi_request')
    def test_should_check_api_to_call_values_to_include_correct_coin(self, mock_get):
        mock_get.return_value = {'BTC': 20000}

        result = get_exchange_rate('BTC')

        self.assertEqual(result, {'BTC': 20000})
        mock_get.assert_called_with('exchangerate/BTC/USD')


class CoinApiTest_get_exchange_rate_history(unittest.TestCase):
    @patch('adapters.coinapi_adapter.coinapi_request')
    def test_should_check_api_to_call_values_to_include_correct_coin(self, mock_get):
        mock_get.return_value = {'BTC': 20000}

        result = get_exchange_rate_history('BTC', '2023-01-10')

        self.assertEqual(result, {'BTC': 20000})
        mock_get.assert_called_with(
            'exchangerate/BTC/USD/history?period_id=1DAY&time_start=2023-01-10T00:00:00')
