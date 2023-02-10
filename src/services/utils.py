def format_currency(response):
    currency_name = response['asset_id_base']
    currency_price = response['rate']
    return (currency_name, '${:,.2f}'.format(currency_price))


def format_currency_name(text):
    return text.upper()
