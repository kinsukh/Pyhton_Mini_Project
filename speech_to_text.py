## requirment : pip install pyttsx3 pyaudio speechrecognition

import pyttsx3
import  speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something:")
        audio = r.listen(source)
        print("Recognizing Now .... ")
        try:
            text  = r.recognize_google(audio)
            print("You have said \n" + text)
            
        except Exception as e:
            print("Error :  " + str(e))

speech_to_text()