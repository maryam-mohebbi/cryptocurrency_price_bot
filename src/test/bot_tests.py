import unittest
from unittest.mock import patch, call
from bot import run, start_bot, setup_exchange, setup_bot


class BotTest_run(unittest.TestCase):
    @patch('bot.start_bot')
    @patch('bot.setup_bot')
    @patch('bot.setup_exchange')
    def test_should_make_sure_all_everything_has_been_set_up_correctly(self, mock_setup_exchange, mock_setup_bot, mock_start_bot):
        # prepare
        mock_setup_exchange.return_value = ''
        mock_setup_bot.return_value = 'MOCK_FN'
        mock_start_bot.return_value = ''

        # run
        run('bot_token', 'coinapi_key', 'coinapi_url')

        # assert
        mock_setup_exchange.assert_called_with('coinapi_url', 'coinapi_key')
        mock_setup_bot.assert_called_with('bot_token')
        mock_start_bot.assert_called_with('MOCK_FN')


class BotTest_start_bot(unittest.TestCase):
    @patch('adapters.telegram_adapter.start')
    def test_should_call_telegram_bot_start(self, mock_telegram_bot_start):
        # prepare
        mock_telegram_bot_start.return_value = ''

        # run
        start_bot('builder')

        # assert
        mock_telegram_bot_start.assert_called_with('builder')


class BotTest_setup_exchange(unittest.TestCase):
    @patch('adapters.coinapi_adapter.setup')
    def test_should_call_exchange_setup(self, mock_exhcnage_setup):
        # prepare
        mock_exhcnage_setup.return_value = ''

        # run
        setup_exchange('api_url', 'api_key')

        # assert
        mock_exhcnage_setup.assert_called_with('api_url', 'api_key')


class BotTest_setup_bot(unittest.TestCase):
    @patch('services.commands.handle_text')
    @patch('services.commands.get_currency_for_chart')
    @patch('services.commands.get_currency_for_price')
    @patch('services.commands.help')
    @patch('services.commands.start')
    @patch('adapters.telegram_adapter.add_message_handler')
    @patch('adapters.telegram_adapter.add_command_handler')
    @patch('adapters.telegram_adapter.setup')
    def test_should_correctly_setup_telegram_bot(
        self, mock_setup, mock_command_handler, mock_message_handler,
        mock_command_start, mock_command_help, mock_command_get_currency_for_price,
        mock_command_get_currency_for_chart, mock_command_handle_text
    ):
        # prepare
        mock_setup.return_value = 'builder'
        mock_command_handler.return_value = ''
        mock_message_handler.return_value = ''

        # run
        setup_bot('bot_token')

        # assert
        mock_setup.assert_called_with('bot_token')
        mock_command_handler.assert_has_calls(
            [
                call('builder', 'start', mock_command_start),
                call('builder', 'help', mock_command_help),
                call('builder', 'price', mock_command_get_currency_for_price),
                call('builder', 'chart', mock_command_get_currency_for_chart),
            ])
        mock_message_handler.assert_called_with(
            'builder', mock_command_handle_text)
