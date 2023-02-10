import traceback
from dateutil.relativedelta import relativedelta
from datetime import date
from services import utils, chart
from adapters import coinapi_adapter as exchange
from adapters import telegram_adapter as bot

get_price_invoked = False
get_chart_invoked = False


async def start(update, context):
    currencies = ['BTC', 'ETH', 'LTC', 'XMR',
                  'TRX', 'BAT', 'MINA', 'ADA', 'DOGE', 'BNB']

    currency_list = []

    for currency_code in currencies:
        response = exchange.get_exchange_rate(currency_code)
        currency_name, currency_price_formatted = utils.format_currency(
            response)
        currency_list.append(
            {'name': currency_name, 'price': currency_price_formatted})

    output = ''
    for item in currency_list:
        output = output + f'''{item['name']}: {item['price']}\n'''

    await bot.reply_text(update, f'''Hello!
Top currency status are as below:

{output}

You always can use /help to see a list of available commands.''')


async def help(update, context):
    await bot.reply_text(update, f'''
Available commands:
/help - List of available commands
/start - Get rate of top currencies
/price - Select a coin and get its price
/chart - Get a chart for selected coin for past 3 months
        ''')


async def show_chart(update, context):
    global get_chart_invoked

    currency_name = utils.format_currency_name(update.message.text)
    date_three_months_ago = date.today() - relativedelta(months=+3)

    try:
        response = exchange.get_exchange_rate_history(
            currency_name, date_three_months_ago)
        buf = chart.draw(currency_name, date_three_months_ago, response)

        # Send the chart image to the user
        buf.seek(0)
        await bot.reply_photo(update, photo=buf)
        # await context.bot.send_photo(chat_id=update.message.chat_id, photo=buf)

    except:
        traceback.print_exc()
        await bot.reply_text(update, f'Invalid currency name entered.')
    get_chart_invoked = False


async def get_currency_for_price(update, context):
    global get_price_invoked
    get_price_invoked = True
    await bot.reply_text(update, f'Which currency rate do you need?')


async def get_currency_for_chart(update, context):
    global get_chart_invoked
    get_chart_invoked = True
    await bot.reply_text(update, f'For which currency do you need a chart?')


async def show_price(update, context):
    global get_price_invoked
    currency_name = utils.format_currency_name(update.message.text)
    try:
        response = exchange.get_exchange_rate(currency_name)
        currency_name, currency_price_formatted = utils.format_currency(
            response)
        await bot.reply_text(update, f'The price of {currency_name} is {currency_price_formatted}.')
    except:
        traceback.print_exc()
        await bot.reply_text(update, f'Invalid currency name entered.')
    get_price_invoked = False


async def handle_text(update, context):
    global get_price_invoked
    global get_chart_invoked
    if get_price_invoked:
        await show_price(update, context)
    elif get_chart_invoked:
        await show_chart(update, context)
    else:
        error_message = 'What do you want to do? Get /help for more information'
        await bot.reply_text(update, error_message)
        return
