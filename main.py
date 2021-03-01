import search,requests
class Quote:
    def __init__(self,symbolOrName):
        try:
            self.symbols=[quote['symbol'] for quote in search.search(symbolOrName)['quotes']]
            self.symbolsQ="%2C".join(self.symbols)
        except:
            raise BaseException("Unable to initiate Quote instance, unable to veryfy symbol")
    def getQuote(self):
        try:
            quote=requests.get(f'https://query2.finance.yahoo.com/v7/finance/quote?lang=en-IN&region=IN&symbols={self.symbolsQ}&fields=longName%2CshortName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CmessageBoardId%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2CregularMarketVolume%2Cuuid%2CregularMarketOpen%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2CtoCurrency%2CfromCurrency%2CtoExchange%2CfromExchange').json()
        except :
            raise BaseException("API error")
        return quote['quoteResponse']['result']
    
    def getHistory(self,p1,p2):
        try:
            quote=requests.get(f'https://query2.finance.yahoo.com/v7/finance/quote?lang=en-IN&region=IN&symbols={self.symbolsQ}&fields=longName%2CshortName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CmessageBoardId%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2CregularMarketVolume%2Cuuid%2CregularMarketOpen%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2CtoCurrency%2CfromCurrency%2CtoExchange%2CfromExchange').json()
        except :
            raise BaseException("API error")
        return quote['quoteResponse']['result']
