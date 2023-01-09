# from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import os
import requests


BOT_TOKEN = os.environ.get('BOT_TOKEN')
X_COINAPI_KEY = os.environ.get('X_COINAPI_KEY')
api_url = 'https://rest.coinapi.io/v1/'
api_headers = {'X-CoinAPI-Key': X_COINAPI_KEY}

builder = ApplicationBuilder().token(BOT_TOKEN).build()


async def start(update, context):
    currencies = ['BTC', 'ETH', 'LTC', 'SOLAR', 'XMR',
                  'TRX', 'BAT', 'MINA', 'ADA', 'DOGE', 'BNB']
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
        f'''
        Hello! You always can use /help to see a list of available commands.
        Top currency status are as below:
        {output}
        '''
    )


builder.add_handler(CommandHandler('start', start))
builder.run_polling()
