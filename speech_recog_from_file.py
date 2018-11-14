#Python 2.x program to transcribe an Audio file 
import speech_recognition as sr
from gtts import gTTS
import os
AUDIO_FILE = ("Recording.wav") 

# use the audio file as the audio source 

r = sr.Recognizer() 

with sr.AudioFile(AUDIO_FILE) as source: 
	#reads the audio file. Here we use record instead of 
	#listen 
	audio = r.record(source) 

try:
    x=r.recognize_google(audio)
    print("The audio file contains: " + x) 

except sr.UnknownValueError: 
	print("Google Speech Recognition could not understand audio") 

except sr.RequestError as e: 
	print("Could not request results from Google Speech Recognition service; {0}".format(e))

language='en'
myobj = gTTS(text=x, lang=language, slow=False)
myobj.save("welcome.wav") 
  
# Playing the converted file 
os.system("mpg321 recording.wav")
