import os
from bot import run


def get_config(config_name):
    return os.environ.get(config_name)


if __name__ == '__main__':
    BOT_TOKEN = get_config('BOT_TOKEN')
    X_COINAPI_KEY = get_config('X_COINAPI_KEY')
    X_COINAPI_URL = get_config('X_COINAPI_URL')

    run(BOT_TOKEN, X_COINAPI_KEY, X_COINAPI_URL)
