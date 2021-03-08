from os import environ
from pydoc import locate

defaultProvider=environ.get('provider',None) or "YahooFinance.YahooFinanceAPI"

def getProvider(provider=defaultProvider):
    return locate(provider)
