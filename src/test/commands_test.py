import unittest
from unittest.mock import patch
from services.commands import help


class BotTest_help(unittest.TestCase):
    @patch('adapters.telegram_adapter.reply_text')
    def test_should_check_calling_reply_text_on_bot_adapter(self, mock_reply_text):
        # prepare
        mock_reply_text.return_value = ''

        # run
        help('update', 'context')

        # assert
        mock_reply_text.assert_called_with('update', f'''
Available commands:
/help - List of available commands
/start - Get rate of top currencies
/price - Select a coin and get its price
/chart - Get a chart for selected coin for past 3 months
        ''')
