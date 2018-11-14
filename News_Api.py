from newsapi import NewsApiClient
from pprint import pprint

# Init
newsapi = NewsApiClient(api_key='9be7514acc8a460e917bf69d71c8791d')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',category='business',language='en',country='us')

all_articles = newsapi.get_everything(sources='bbc-news,the-verge',domains='bbc.co.uk,techcrunch.com',from_param='2018-11-01',to='2018-11-12',language='en',sort_by='relevancy',page=2)

pprint(all_articles)
