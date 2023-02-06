import unittest
from bot import get_config, format_currency, format_currency_name
import os


class BotTest_get_config(unittest.TestCase):
    def test_should_return_correct_value_from_os_environ(self):
        # prepare
        os.environ['test_config'] = 'test_value'

        # run
        result = get_config('test_config')

        # assert
        self.assertEqual(result, 'test_value')


class BotTest_format_currency(unittest.TestCase):
    def test_should_return_formatted_currency_name_and_price(self):
        # prepare
        response = {'asset_id_base': 'btc', 'rate': 20000}

        # run
        result = format_currency(response)

        # assert
        self.assertEqual(result, ('btc', '$20,000.00'))


class BotTest_format_currency_name(unittest.TestCase):
    def test_should_return_uppercase_currency_name(self):
        # prepare
        text = 'btc'

        # run
        result = format_currency_name(text)

        # assert
        self.assertEqual(result, 'BTC')
