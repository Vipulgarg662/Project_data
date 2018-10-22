import speech_recognition as sr

def findpronoun(text):
    for i in text.sentences:
        pr=find_pronoun(i)
        no=find_noun(i)
        ve=find_verb(i)
        adj=find_adjective(i)
    print("pronoun : "+pr+" noun : "+n+" verb : "+ve+" adjective : "+adj)
r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print ("Say Something")
    audio=r.listen(source)

    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
print(text)
findpronoun(text)


