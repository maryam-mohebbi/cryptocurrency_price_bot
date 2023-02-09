import traceback
from dateutil.relativedelta import relativedelta
from datetime import date
from datetime import datetime
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib

from adapters import coinapi_adapter as exchange
from adapters import telegram_adapter as bot
matplotlib.use('Agg')

get_price_invoked = False
get_chart_invoked = False


def format_currency(response):
    currency_name = response['asset_id_base']
    currency_price = response['rate']
    return (currency_name, '${:,.2f}'.format(currency_price))


def format_currency_name(text):
    return text.upper()


async def start(update, context):
    currencies = ['BTC', 'ETH', 'LTC', 'XMR',
                  'TRX', 'BAT', 'MINA', 'ADA', 'DOGE', 'BNB']

    currency_list = []

    for currency_code in currencies:
        response = exchange.get_exchange_rate(currency_code)
        currency_name, currency_price_formatted = format_currency(response)
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
    currency_name = format_currency_name(update.message.text)
    try:
        response = exchange.get_exchange_rate(currency_name)
        currency_name, currency_price_formatted = format_currency(response)
        await bot.reply_text(update, f'The price of {currency_name} is {currency_price_formatted}.')
    except:
        traceback.print_exc()
        await bot.reply_text(update, f'Invalid currency name entered.')
    get_price_invoked = False


def chart_data_process(response):
    rate_closes = [item['rate_close'] for item in response]
    time_closes = [item['time_close'].split('.')[0] for item in response]
    time_closes = [datetime.strptime(
        time_closes[i], '%Y-%m-%dT%H:%M:%S') for i in range(len(time_closes))]
    return rate_closes, time_closes


def plot_data(rate_closes, time_closes, currency_name, date_three_months_ago):
    # Clean memory of past charts
    plt.clf()

    plt.plot(rate_closes)

    # Show x-lab for every 7 days
    interval = 7

    plt.xticks(range(0, len(time_closes), interval), [time_closes[i].strftime(
        '%Y-%m-%d') for i in range(0, len(time_closes), interval)], rotation=90)
    plt.xlabel('Period')
    plt.ylabel('Rate Close')
    plt.title(f'{currency_name} rate changes from {date_three_months_ago}')

    # Save the chart to a memory buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    return buf


async def show_chart(update, context):
    global get_chart_invoked

    currency_name = format_currency_name(update.message.text)
    date_three_months_ago = date.today() - relativedelta(months=+3)

    try:
        response = exchange.get_exchange_rate_history(
            currency_name, date_three_months_ago)
        rate_closes, time_closes = chart_data_process(response)
        if not rate_closes:
            raise ValueError('Invalid currency name entered.')
        buf = plot_data(rate_closes, time_closes,
                        currency_name, date_three_months_ago)

        # Send the chart image to the user
        buf.seek(0)
        await bot.reply_photo(update, photo=buf)
        # await context.bot.send_photo(chat_id=update.message.chat_id, photo=buf)

    except:
        traceback.print_exc()
        await bot.reply_text(update, f'Invalid currency name entered.')
    get_chart_invoked = False


async def find_function(update, context):
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


def setup_bot(token):
    builder = bot.setup(token)
    bot.add_command_handler(builder, 'start', start)
    bot.add_command_handler(builder, 'help', help)
    bot.add_command_handler(builder, 'price', get_currency_for_price)
    bot.add_command_handler(builder, 'chart', get_currency_for_chart)

    bot.add_message_handler(builder, find_function)
    return builder


def setup_exchange(api_url, key):
    exchange.setup(api_url, key)


def start_bot(builder):
    bot.start(builder)


def run(BOT_TOKEN, X_COINAPI_KEY, X_COINAPI_URL):
    setup_exchange(X_COINAPI_URL, X_COINAPI_KEY)

    builder = setup_bot(BOT_TOKEN)
    start_bot(builder)
