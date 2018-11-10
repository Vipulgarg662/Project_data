import requests
from pprint import pprint
from PIL import Image
from io import BytesIO

movie=input("Enter Movie name: ")
#search for the movie 
url="https://api.themoviedb.org/3/search/movie?api_key=db8e8a335f61868e2fec825406e85134&query="+movie
res=requests.get(url)
data=res.json()

#extract movie id
movie_id=data['results'][1]['id']

#extract poster path
poster_path=data['results'][1]['poster_path']

#url for the poster
Poster_url="https://image.tmdb.org/t/p/w154/"+poster_path
res_poster=requests.get(Poster_url)
#extract poster from api
img=Image.open(BytesIO(res_poster.content))
#view image
img.show()

#url for movie data through id
Movie_url="https://api.themoviedb.org/3/movie/{}?api_key=db8e8a335f61868e2fec825406e85134".format(movie_id)
res_movie=requests.get(Movie_url)
data2=res_movie.json()

#print movie data extracted
pprint(data2)




