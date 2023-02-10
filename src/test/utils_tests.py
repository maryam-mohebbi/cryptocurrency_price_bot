import unittest
from services.utils import format_currency, format_currency_name


class UtilsTest_format_currency(unittest.TestCase):
    def test_should_return_formatted_currency_name_and_price(self):
        # prepare
        response = {'asset_id_base': 'btc', 'rate': 20000}

        # run
        result = format_currency(response)

        # assert
        self.assertEqual(result, ('btc', '$20,000.00'))


class UtilsTest_format_currency_name(unittest.TestCase):
    def test_should_return_uppercase_currency_name(self):
        # prepare
        text = 'btc'

        # run
        result = format_currency_name(text)

        # assert
        self.assertEqual(result, 'BTC')
