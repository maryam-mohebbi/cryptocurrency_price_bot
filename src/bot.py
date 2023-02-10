from adapters import coinapi_adapter as exchange
from adapters import telegram_adapter as bot
from services import commands


def setup_bot(token):
    builder = bot.setup(token)
    bot.add_command_handler(builder, 'start', commands.start)
    bot.add_command_handler(builder, 'help', commands.help)
    bot.add_command_handler(builder, 'price', commands.get_currency_for_price)
    bot.add_command_handler(builder, 'chart', commands.get_currency_for_chart)

    bot.add_message_handler(builder, commands.handle_text)
    return builder


def setup_exchange(api_url, key):
    exchange.setup(api_url, key)


def start_bot(builder):
    bot.start(builder)


def run(BOT_TOKEN, X_COINAPI_KEY, X_COINAPI_URL):
    setup_exchange(X_COINAPI_URL, X_COINAPI_KEY)

    builder = setup_bot(BOT_TOKEN)
    start_bot(builder)
