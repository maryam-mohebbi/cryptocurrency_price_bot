# Example Improvment on Clean Code

## PEP 8 (Python Enhancement Proposal)

PEP 8 is a style guide that describes the coding standards for Python. It's the most popular guide within the Python community
It's containe 4 rolls category:  
PEP 8 naming conventions
PEP 8 line formatting
PEP 8 whitespace
PEP 8 comments

### Before:

```
api_url = 'https://rest.coinapi.io/v1/'
endpoint = f"exchangerate/{currency}/USD"
```

### After:

```
api_url = 'https://rest.coinapi.io/v1/'
endpoint = f'exchangerate/{currency}/USD'
```

## DRY

### Before:

Calling API lines repeated in each part of code. I make two function for prevent the repitation and make more redability for further changes

```
endpoint = f"exchangerate/{currency}/USD"
response = requests.get(api_url + endpoint, headers=api_headers).json()
```

### After:

```
def get_exchange_rate(currency_name):
    endpoint = f'exchangerate/{currency_name}/USD'
    response = coinapi_request(endpoint)
    return response

def coinapi_request(endpoint):
    api_headers = {'X-CoinAPI-Key': X_COINAPI_KEY}
    response = requests.get(API_URL + endpoint, headers=api_headers).json()
    return response
```

## KISS

### Before:

Initially, all the setup functions were being called from the main method. I broke the code into multiple functions with meaningful names and now, when one reads the `run` function, they can easily understand what it does.

### After:

```
def run(BOT_TOKEN, X_COINAPI_KEY, X_COINAPI_URL):
    setup_exchange(X_COINAPI_URL, X_COINAPI_KEY)

    builder = setup_bot(BOT_TOKEN)
    start_bot(builder)
```

## SRP (Single Responsibility Principle)

Before applying SRP, there were instances that the code was getting the exchange rate from the exchange and in the same method, it was replying to the customer.
I created a new method called `get_exchange_rate` and took it out of the code. This function now only does one task.
There were multiple instances of such behaviour that I improved.

## Dependency Inversion Principle

In my codebase, internal modules (directories) do not import from the upper modules. I followed this principle when I was designing my modules architecture.
