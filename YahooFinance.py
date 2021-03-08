from requests import get as fetch

from quoteProvider import Provider

from datetime import datetime
from csv import DictReader

class YahooFinanceAPI(Provider):
    @staticmethod
    def __encode(symbolOrNames):
        if isinstance(symbolOrNames, list):
            # dummy entry to force comma, so as to trigger maped result
            symbolOrNames = [*symbolOrNames, "@"]
            symbolOrNames = "%2C".join(symbolOrNames)
        return symbolOrNames

    def getQuoteLatest(self, symbolOrNames):
        results=self.getQuoteLatestResponse(symbolOrNames)['quoteResponse']['result']
        def select(res):
                Date=datetime.fromtimestamp(res['regularMarketTime']-86400 if res['quoteSourceName']== 'Delayed Quote' else res['regularMarketTime']).strftime("%Y-%m-%d")
                Open= res['regularMarketOpen']
                Close= res['regularMarketPrice']
                High= res['regularMarketDayHigh']
                Low= res['regularMarketDayLow']
                Adj= res['regularMarketAdjustedClose'] if 'regularMarketAdjustedClose' in res else Close
                Volume=res['regularMarketVolume']
                Symbol= res['symbol']
                return {'Symbol':Symbol,'Date':Date,'Open':Open,'High':High,'Low':Low,'Close':Close,'Adj Close':Adj,'Volume':Volume}
        return [select(result) for result in results]

    def verifySymbol(self, symbolOrNames):
        res = self.getSearchResponse(symbolOrNames)
        return [entity['symbol'] for entity in res['quotes']]
    def getQuoteHistory(self,symbol,p1=1583005374, p2=None):
        inter=[csv.split('\n') for csv in self.getQuoteHistoryResponse(symbol,p1,p2)]
        return [DictReader(csv) for csv in inter]
    def getQuoteHistoryResponse(self, symbol, p1=1583005374, p2=None):
        if not p2:
            p2 = p1
        symbols = self.verifySymbol(symbol)
        def download(symbol): return fetch(
            f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={p1}&period2={p2}&interval=1d&events=history&includeAdjustedClose=true').text
        return [download(sym) for sym in symbols]

    def getSearchResponse(self, symbolOrNames):
        symbolOrNames = Provider._ensureList(symbolOrNames)
        symbolsEncoded = self.__encode(symbolOrNames)
        res = fetch(
            f"https://query2.finance.yahoo.com/v1/finance/search?q={symbolsEncoded}&quotesCount=1&newsCount=0&enableFuzzyQuery=false&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId=multi_quote_single_token_query&newsQueryId=news_ss_symbols&enableCb=false&enableNavLinks=false").json()
        return res

    def getQuoteLatestResponse(self, symbolOrNames):
        symbolOrNames = self.verifySymbol(symbolOrNames)
        symbolsEncoded = self.__encode(symbolOrNames)
        quote = fetch(
            f'https://query2.finance.yahoo.com/v7/finance/quote?lang=en-IN&region=IN&symbols={symbolsEncoded}&fields=longName%2CshortName%2CregularMarketPrice%2CregularMarketChange%2CregularMarketChangePercent%2CmessageBoardId%2CmarketCap%2CunderlyingSymbol%2CunderlyingExchangeSymbol%2CheadSymbolAsString%2CregularMarketVolume%2Cuuid%2CregularMarketOpen%2CfiftyTwoWeekLow%2CfiftyTwoWeekHigh%2CtoCurrency%2CfromCurrency%2CtoExchange%2CfromExchange').json()
        return quote
# p=YahooFinance()
# print([list(d) for d in p.getQuoteHistory('ONGC.NS',1612351202)])