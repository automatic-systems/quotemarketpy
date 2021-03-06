from abc import ABC, abstractmethod ,ABCMeta
class Provider(metaclass=ABCMeta):
    @staticmethod
    def _ensureList(symbol):
        return symbol if isinstance(symbol,list) else [symbol]
    @abstractmethod
    def verifySymbol(self,symbolOrName):
        '''
            symbolOrName: symbol or name of the entity, or a list of symbol or name
            returns-> list of valid symbol for the given enitity
        '''
        pass

    @abstractmethod
    def getQuoteLatest(self,symbolsorNames):
        '''
            symbolOrName: symbol or name of the entity, or a list of symbol or name
            returns-> returns list of dictionary {symbol,Date,Open,High,Low,Close,Adj Close,Volume}
        '''
        pass
    
    @abstractmethod
    def getQuoteHistory(self,symbolsorNames,p1,p2):
        '''
            symbolOrName: symbol or name of the entity, or a list of symbol or name
            returns-> returns list of (list of dictionary {symbol,Date,Open,High,Low,Close,Adj Close,Volume})
        '''
        pass