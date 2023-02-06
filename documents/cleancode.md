# Clean Code Cheetsheet

# PEP 8 (Python Enhancement Proposal)

PEP 8 is a style guide that describes the coding standards for Python. It's the most popular guide within the Python community
It's containe 4 rolls category:  
PEP 8 naming conventions
PEP 8 line formatting
PEP 8 whitespace
PEP 8 comments

Before:

```
api_url = 'https://rest.coinapi.io/v1/'
endpoint = f"exchangerate/{currency}/USD"
```

After:

```
api_url = 'https://rest.coinapi.io/v1/'
endpoint = f'exchangerate/{currency}/USD'
```

# DRY (Don't repeat yourself)

Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

before:
calling API lines repeated in each part of code. I make two function for prevent the repitation and make more redability for further changes

```
endpoint = f"exchangerate/{currency}/USD"
response = requests.get(api_url + endpoint, headers=api_headers).json()
```

after:

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

# KISS (Keep it simple, stupid)

Most systems work best if they are kept simple, rather than made complicated.

# SoC (Separation of Concerns)

SoC is a design principle for separating a computer program into distinct sections such that each section addresses a separate concern. A concern is a set of information that affects the code of a computer program.

before: There was a single file with all function
after : I seprated the coin API part to another file named 'coinapi_adapter.py' and moved function into it.

# SOLID

SOLID is a mnemonic acronym for five design principles intended to make software designs more understandable, flexible, and maintainable.

## The Single-responsibility principle:

"A class should have one, and only one, reason to change."

## The Open–closed principle:

"Entities should be open for extension, but closed for modification."

## The Liskov substitution principle:

"Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."

## The Interface segregation principle:

"A client should not be forced to implement an interface that it doesn’t use."

## The Dependency inversion principle:

"Depend upon abstractions, not concretions."
