# quotemarketpy
Easily get a quote for any Entity from any market for any date.

# USAGE:
## Import:
```python
from stockcli import getProvider

'''
  def getProvider(provider=defaultProvider):: where provider can be either of 
  "YahooFinance.YahooFianceAPI", "MoneyControl.MoneyControlBrowser", "YahooFinance.YahooFianceBrowser"
'''

```

### Execute:
```python

providerClass=getProvider("YahooFinance.YahooFinanceAPI") ''' optional argument '''

'''
 or
    providerClass=getProvider("MoneyControl.MoneyControlBrowser") 
    providerClass=getProvider("YahooFinance.YahooFianceBrowser") 
'''  
```

### Output:
```python
provider=providerClass()

provider.getQuoteLatest("yes bank")
`
  [{'Symbol': 'YESBANK.NS',
  'Date': '2021-03-08',
  'Open': 16.55,
  'High': 16.65,
  'Low': 16.4,
  'Close': 16.4,
  'Adj Close': 16.4,
  'Volume': 40674074}]
`

provider.getQuoteLatest(["HDFC Bank","ONGC.NS"])
`
[{'Symbol': 'HDB',
  'Date': '2021-03-05',
  'Open': 82.17,
  'High': 82.47,
  'Low': 80.01,
  'Close': 82.28,
  'Adj Close': 82.28,
  'Volume': 1587889},
 {'Symbol': 'ONGC.NS',
  'Date': '2021-03-08',
  'Open': 118.95,
  'High': 122.35,
  'Low': 117.8,
  'Close': 118.85,
  'Adj Close': 118.85,
  'Volume': 49324173}]
`

''' history data for HDFCBANK and `Axis Midcap Fund Direct Plan Growth` from 1 march to 8 march '''
HDFC,axisMutualFund=  pro.getQuoteHistory(["HDB",'yes bank'],1596871142,1615187942)
[*axisMutualFund]
`[{'Date': '2021-03-01',
  'Open': '59.700001',
  'High': '59.700001',
  'Low': '59.700001',
  'Close': '59.700001',
  'Adj Close': '59.700001',
  'Volume': '0'},
 {'Date': '2021-03-02',
  'Open': '60.740002',
  'High': '60.740002',
  'Low': '60.740002',
  'Close': '60.740002',
  'Adj Close': '60.740002',
  'Volume': '0'},
 {'Date': '2021-03-03',
  'Open': '61.610001',
  'High': '61.610001',
  'Low': '61.610001',
  'Close': '61.610001',
  'Adj Close': '61.610001',
  'Volume': '0'},
 {'Date': '2021-03-04',
  'Open': '61.650002',
  'High': '61.650002',
  'Low': '61.650002',
  'Close': '61.650002',
  'Adj Close': '61.650002',
  'Volume': '0'},
 {'Date': '2021-03-05',
  'Open': '60.910000',
  'High': '60.910000',
  'Low': '60.910000',
  'Close': '60.910000',
  'Adj Close': '60.910000',
  'Volume': '0'},
 {'Date': '2021-03-08',
  'Open': 'null',
  'High': 'null',
  'Low': 'null',
  'Close': 'null',
  'Adj Close': 'null',
  'Volume': 'null'}]
`

[*HDFC]
`
.
.

`
```

## More Methods:
- `def verifiySymbol(symbolsornames)`

# TODO
- implement the follwoing:
  - `MoneyControl.*`
  - `YahooFinance.YahooFinanceBrowser`
