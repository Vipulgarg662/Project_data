from tkinter import *
import speech_recognition as sr
import requests
import webbrowser
import os
import re
from gtts import gTTS

def Weather_Status(city):
    url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=2bca5db701a487480073a7661ff4e481&units=metric".format(city)
    res=requests.get(url)
    data=res.json()
    print("Location       :",data['name'])
    print('temperature    :',data['main']['temp'],"C")
    print("humidity       :",data['main']['humidity'])
    print("Weather Status :",data['weather'][0]['description'])
    print("Wind Speed     :",data['wind']['speed'],'m/s')

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
    print("Released Date :",data['Released'])
    print("Runtime       :",data['Runtime'])
    print("Awards        :",data['Awards'])
    print("BoxOffice Coll:",data['BoxOffice'])
    print("Country       :",data['Country'])
    print("Imdb Rating   :",data['imdbRating'])
    print("Plot          :",data['Plot'])
    
def Open_website(a):
    url="https://www."+a
    webbrowser.open(url)

def Open_apps(a):
    os.system("start {}".format(a))

def System_shutdown(a):
    if a=='shutdown':
        os.system("shutdown -s")
    elif a=='restart':
        os.system("shutdown -r")
    else:
        os.system("shutdown -l")

def Speech_to_text():
    mic=sr.Microphone()
    r = sr.Recognizer()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print("You said : ",text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return text

def Text_to_speech(x):
    print(x)
    #language='en'
    #myobj = gTTS(text=x, lang=language)
    #myobj.save("output.mp3") 
    #os.system("output.wav")
    
def assistant(text):
    if 'movie' in text:
        reg=re.search('(.*) (.*)',text)
        movie=reg.group(2)
        Movie_Info(movie)
    elif 'weather' in text:
        reg=re.search('(.*)weather in (.*)',text)
        city=reg.group(2)
        if(city=='my city'):
            city='meerut'
        Weather_Status(city)
    
    elif 'open app' in text:
        reg=re.search('open app (.*)',text)
        app=reg.group(1)
        Open_apps(app)

    elif 'open website' in text:
        reg=re.search('open website (.*)',text)
        website=reg.group(1)
        Open_website(website)

    elif 'my computer' in text:
        reg=re.search('(.*) my .*',text)
        command=reg.group(1)
        System_shutdown(command)

    elif 'exit' in text:
        return 'exit'


#root=Tk()
while(1):
    Text_to_speech("Tell me what to do")
    a=assistant(Speech_to_text())
    if a=='exit':
        break
    
    
    

