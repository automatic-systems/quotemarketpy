import requests

def search(search):
            if isinstance(search,list):
                search.append("@") # dummy entry to force comma, so as to trigger maped result
                search="%2C".join(search)
            res=requests.get(f"https://query2.finance.yahoo.com/v1/finance/search?q={search}&quotesCount=1&newsCount=0&enableFuzzyQuery=false&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId=multi_quote_single_token_query&newsQueryId=news_ss_symbols&enableCb=false&enableNavLinks=false").json()
            # if  not res.error == 'null':
            #     raise BaseException("API Error")
            return res
