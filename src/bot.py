from datetime import datetime
from io import BytesIO
import matplotlib.pyplot as plt
from telegram.ext import ApplicationBuilder, CommandHandler, filters, MessageHandler
import os
import requests
import matplotlib
matplotlib.use('Agg')


BOT_TOKEN = os.environ.get('BOT_TOKEN')
X_COINAPI_KEY = os.environ.get('X_COINAPI_KEY')
api_url = 'https://rest.coinapi.io/v1/'
api_headers = {'X-CoinAPI-Key': X_COINAPI_KEY}

builder = ApplicationBuilder().token(BOT_TOKEN).build()


async def start(update, context):
    currencies = ['BTC', 'ETH', 'LTC', 'XMR']
#  , 'TRX', 'BAT', 'MINA', 'ADA', 'DOGE', 'BNB']

    currency_list = []

    for currency in currencies:
        endpoint = f"exchangerate/{currency}/USD"
        response = requests.get(api_url + endpoint, headers=api_headers).json()
        name = response["asset_id_base"]
        price = response["rate"]
        price_formatted = "${:,.2f}".format(price)
        currency_list.append({'name': name, 'price': price_formatted})

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
/chart - Get a chart for selected coins
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
    endpoint = f"exchangerate/{currency_name}/USD"
    try:
        response = requests.get(api_url + endpoint, headers=api_headers).json()
        name = response["asset_id_base"]
        price = response["rate"]
        price_formatted = "${:,.2f}".format(price)
        await update.message.reply_text(
            f"The price of {name} is {price_formatted}."
        )
    except:
        await update.message.reply_text(
            f"Invalid currency name entered."
        )
    get_price_invoked = False


async def draw_chart(update, context):
    global get_chart_invoked

    endpoint = f"exchangerate/BTC/USD/history?period_id=1DAY&time_start=2022-12-01T00:00:00"
    response = requests.get(api_url + endpoint, headers=api_headers).json()

    rate_closes = [item['rate_close'] for item in response]
    time_closes = [item['time_close'].split(".")[0] for item in response]
    time_closes = [datetime.strptime(
        time_closes[i], '%Y-%m-%dT%H:%M:%S') for i in range(len(time_closes))]

    plt.plot(rate_closes)
    interval = 3
    plt.xticks(range(0, len(time_closes), interval), [time_closes[i].strftime(
        '%Y-%m-%d') for i in range(0, len(time_closes), interval)], rotation=90)
    plt.xlabel('Period')
    plt.ylabel('Rate Close')

    # Save the chart to a memory buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')

    # Send the chart image to the user
    buf.seek(0)
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=buf)
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
