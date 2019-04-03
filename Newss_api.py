import requests
from pprint import pprint
#top headlkines
url="https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=9be7514acc8a460e917bf69d71c8791d"

#everything
url2="https://newsapi.org/v2/everything?sources=the-times-of-india&apiKey=9be7514acc8a460e917bf69d71c8791d"
res=requests.get(url)

#particular topic
url3="https://newsapi.org/v2/everything?q=bitcoin&apiKey=9be7514acc8a460e917bf69d71c8791d"
data=res.json()
pprint(data)
