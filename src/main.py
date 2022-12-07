def user_gateway():
    user_input = user_gateway_input('cli')
    output = core(user_input)
    return output


def core(command):
    if command == '/start':
        prices = marketplace_get_prices()
        return prices
    else:
        return 'Invalid command'


def marketplace():
    return


def marketplace_get_prices():
    btc = '16,000 EUR'
    eth = '1,200 EUR'
    coins_list = {'btc': btc, 'eth': eth}
    return coins_list


def user_gateway_input(method):
    if method == 'cli':
        user_input = input('Enter command: ')
        return user_input

    elif method == 'telegram':
        # Here we should impliment Telegram input
        return


output = user_gateway()
print(output)
