import requests
from pprint import pprint

movie=input("movie name : ")
url="http://www.omdbapi.com/?t={}&apikey=44115df3".format(movie)
res=requests.get(url)
data=res.json()
pprint(data)
post=data['Poster']

typ=data['Type']
rel=data['Released']
cast=data['Actors']
plot=data['Plot']
rate=data['imdbRating']
print(typ,rel,cast,plot,rate,sep="\n")
