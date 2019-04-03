import requests
from pprint import pprint
#taking city name from user
city=input("Enter City")

#Api url which contains the url
#q is taking city name
#appid is special key for every user
#unit for tempearature unit
url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=2bca5db701a487480073a7661ff4e481&units=metric".format(city)

res=requests.get(url)

#convert data into json format for view
data=res.json()

#pprint is used to print in special managed format
pprint(data)

#to print a particular value
temp=data['main']['temp']
hum=data['main']['humidity']
weather=data['weather'][0]['description']
wind=data['wind']['speed']
print("Location       :",data['name'])
print('temperature    :',temp,"C")
print("humidity       :",hum)
print("Weather Status :",weather)
print("Wind Speed     :",wind)


