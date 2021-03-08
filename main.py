defaultProvider="YahooFinance.YahooFinance"

from os import environ
from pydoc import locate

provider=locate(environ.get('provider','#')) or locate(defaultProvider)
