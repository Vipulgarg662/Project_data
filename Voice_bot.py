import speech_recognition as sr
import requests


def Weather_Status(city):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=2bca5db701a487480073a7661ff4e481&units=metric".format(city)
    res=requests.get(url)
    data=res.json()
    temp=data['main']['temp']
    hum=data['main']['humidity']
    weather=data['weather'][0]['description']
    wind=data['wind']['speed']
    print("Location       :",data['name'])
    print('temperature    :',temp,"C")
    print("humidity       :",hum)
    print("Weather Status :",weather)
    print("Wind Speed     :",wind)

def Movie_Info(movie):
    url="http://www.omdbapi.com/?t={}&apikey=44115df3".format(movie)
    res=requests.get(url)
    data=res.json()
    print("Title         :",data['Title'])
    print("Actors        :",data['Actors'])
    print("Director      :",data['Director'])
    print("Writer        :",data['Writer'])
    print("Genre         :",data['Genre'])
    print("Language      :",data['Language'])
    print("Production    :",data['Production'])
    print("Released Date :",=data['Released'])
    print("Runtime       :",data['Runtime'])
    print("Awards        :",data['Awards'])
    print("BoxOffice Coll:",data['Boxoffice'])
    print("Country       :",data['Country'])
    print("Imdb Rating   :"data['imdbRating'])
    print("Plot          :",data['Plot'])
    


#creating an instance for Microphone class
mic=sr.Microphone()

#Initialize the recognizer 
r = sr.Recognizer() 

#use the microphone as source for input.  
with mic as source: 
	#wait for a second to let the recognizer adjust the 
	#energy threshold based on the surrounding noise level 
	r.adjust_for_ambient_noise(source) 
	print ("Say Something: ")
	#listens for the user's input 
	audio = r.listen(source) 
		
	try: 
		text = r.recognize_google(audio)  
	
	#error occurs when google could not understand what was said
	except sr.UnknownValueError: 
		print("Google Speech Recognition could not understand audio") 
	
	except sr.RequestError as e: 
		print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
