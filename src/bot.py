import traceback
from dateutil.relativedelta import relativedelta
from datetime import date
from datetime import datetime
from io import BytesIO
import matplotlib.pyplot as plt
from telegram.ext import ApplicationBuilder, CommandHandler, filters, MessageHandler
import os
from adapters import coinapi_adapter as exchange
import matplotlib
matplotlib.use('Agg')


def get_config(config_name):
    return os.environ.get(config_name)


BOT_TOKEN = get_config('BOT_TOKEN')
X_COINAPI_KEY = get_config('X_COINAPI_KEY')
API_URL = get_config('API_URL')

exchange.setup(API_URL, X_COINAPI_KEY)

builder = ApplicationBuilder().token(BOT_TOKEN).build()


async def start(update, context):
    currencies = ['BTC', 'ETH', 'LTC', 'XMR',
                  'TRX', 'BAT', 'MINA', 'ADA', 'DOGE', 'BNB']

    currency_list = []

    for currency_code in currencies:
        response = exchange.get_exchange_rate(currency_code)
        currency_name = response['asset_id_base']
        currency_price = response['rate']
        currency_price_formatted = '${:,.2f}'.format(currency_price)
        currency_list.append(
            {'name': currency_name, 'price': currency_price_formatted})

    output = ''
    for item in currency_list:
        output = output + f'''{item['name']}: {item['price']}\n'''

    await update.message.reply_text(
        f'''Hello!
Top currency status are as below:

{output}

You always can use /help to see a list of available commands.'''
    )


async def help(update, context):
    await update.message.reply_text(
        f'''
Available commands:
/help - List of available commands
/start - Get rate of top currencies
/getPrice - Select a coin and get its price
/chart - Get a chart for selected coin for past 3 months
        '''
    )


get_price_invoked = False
get_chart_invoked = False


async def get_currency_for_price(update, context):
    global get_price_invoked
    get_price_invoked = True
    await update.message.reply_text(
        f'Which currency rate do you need?'
    )


async def get_currency_for_chart(update, context):
    global get_chart_invoked
    get_chart_invoked = True
    await update.message.reply_text(
        f'For which currency do you need a chart?'
    )


async def show_price(update, context):
    global get_price_invoked
    currency_name = update.message.text
    currency_name = currency_name.upper()
    try:
        response = exchange.get_exchange_rate(currency_name)
        currency_name = response['asset_id_base']
        currency_price = response['rate']
        currency_price_formatted = '${:,.2f}'.format(currency_price)
        await update.message.reply_text(
            f'The price of {currency_name} is {currency_price_formatted}.'
        )
    except:
        traceback.print_exc()
        await update.message.reply_text(
            f'Invalid currency name entered.'
        )
    get_price_invoked = False


async def draw_chart(update, context):
    global get_chart_invoked

    currency_name = update.message.text
    currency_name = currency_name.upper()
    date_three_months_ago = date.today() - relativedelta(months=+3)

    try:
        response = exchange.get_exchange_rate_history(
            currency_name, date_three_months_ago)
        rate_closes = [item['rate_close'] for item in response]
        time_closes = [item['time_close'].split('.')[0] for item in response]
        time_closes = [datetime.strptime(
            time_closes[i], '%Y-%m-%dT%H:%M:%S') for i in range(len(time_closes))]

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

        # Send the chart image to the user
        buf.seek(0)
        await context.bot.send_photo(chat_id=update.message.chat_id, photo=buf)

    except:
        traceback.print_exc()
        await update.message.reply_text(
            f'Invalid currency name entered.'
        )
    get_chart_invoked = False


async def find_function(update, context):
    global get_price_invoked
    global get_chart_invoked
    if get_price_invoked:
        await show_price(update, context)
    elif get_chart_invoked:
        await draw_chart(update, context)
    else:
        error_message = 'What do you want to do? Get /help for more information'
        await update.message.reply_text(error_message)
        return


builder.add_handler(CommandHandler('start', start))
builder.add_handler(CommandHandler('help', help))
builder.add_handler(CommandHandler('getPrice', get_currency_for_price))
builder.add_handler(CommandHandler('chart', get_currency_for_chart))

find_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), find_function)
builder.add_handler(find_handler)

builder.run_polling()
