import speech_recognition as sr
import requests
import webbrowser
import os
import re
import win32com.client as wincl
import geocoder
import smtplib
import wikipedia


def loc():
    g = geocoder.ip('me')
    return(g.city)




def Weather_Status(city):
    city=loc()
    url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=2bca5db701a487480073a7661ff4e481&units=metric".format(city)
    res=requests.get(url)
    data=res.json()
    #print("Location       :",data['name'])
    print('temperature    :',data['main']['temp'],"C")
    print("humidity       :",data['main']['humidity'])
    print("Weather Status :",data['weather'][0]['description'])
    print("Wind Speed     :",data['wind']['speed'],'m/s')
    Text_to_speech("Current weather in %s is %s the temperature is %.lf degree celsius"%(data['name'],data['weather'][0]['description'],data['main']['temp']))





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
    #print("Plot          :",data['Plot'])
    Text_to_speech("Plot          :%s"%data['Plot'])
    Text_to_speech("This is all i got about movie %s"%(data['Title']))
    




def Open_website(a):
    url="https://www."+a+".com"
    webbrowser.open(url)
    Text_to_speech("Done")






def Open_apps(a):
    os.system("start {}".format(a))
    Text_to_speech("Done")




def Close_apps(a):
    os.system("taskkill /F /IM {}.exe".format(a))
    Text_to_speech("Done")




def wiki(a):
    try:
        data=wikipedia.summary(data)
        Text_to_speech(data)
    except wikipedia.exceptions.DisambiguationError as e:
        Text_to_speech('Please be more specified')



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
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print(text)
            return text
        except sr.UnknownValueError:
            Text_to_speech("Sorry, I am not able to understand what you said")
            Text_to_speech('Tell me what to do!!')
        except sr.RequestError as e:
            Text_to_speech("Could not request results from Google Speech Recognition service; {0}".format(e))



        

def Text_to_speech(x):
    print(x)
    speak=wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(x)




    
def assistant(text):
    if 'movie' in text:
        reg=re.search('(.*) (.*)',text)
        movie=reg.group(2)
        Movie_Info(movie)
    elif 'weather' in text:
        reg=re.search('(.*) (.*)',text)
        city=reg.group(2)
        if(city=='my city'):
            city='meerut'
        Weather_Status(city)
    
    elif 'open app' in text:
        reg=re.search('open app (.*)',text)
        app=reg.group(1)
        Open_apps(app)

    elif 'close app' in text:
        reg=re.search('close app (.*)',text)
        app=reg.group(1)
        Close_apps(app)

    elif 'open website' in text:
        reg=re.search('open website (.*)',text)
        website=reg.group(1)
        Open_website(website)

    elif 'my computer' in text:
        reg=re.search('(.*) my .*',text)
        command=reg.group(1)
        System_shutdown(command)

    elif 'exit' in text:
        Text_to_speech("See you next time, bye")
        return 'exit'

    elif 'tell me a joke' in text:
        responeData = requests.get("http://api.icndb.com/jokes/random/?escape=javascript")
        joke = str(responeData.json()['value']['joke'])
        Text_to_speech(joke)

    elif 'what is' in text:
        reg=re.search('what is (.*)',text)
        data=reg.group(1)
        wiki(data)

    Text_to_speech('Tell me what to do!!')




Text_to_speech("Tell me what to do!!")
while True:
    text=Speech_to_text()
    if text:
        text=text.lower()
        a=assistant(text)
        if a=='exit':
            print('Good Bye')
            break
    
    
    

