# from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
import os
import requests
from telegram.ext import filters, MessageHandler


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
        '''
    )


async def get_price(update, context):
    await update.message.reply_text(
        f''' Which currency rate do you need?'''
    )


async def find_price(update, context):
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


builder.add_handler(CommandHandler('start', start))
builder.add_handler(CommandHandler('help', help))
builder.add_handler(CommandHandler('getPrice', get_price))
find_price_handler = MessageHandler(
    filters.TEXT & (~filters.COMMAND), find_price)
builder.add_handler(find_price_handler)

builder.run_polling()
