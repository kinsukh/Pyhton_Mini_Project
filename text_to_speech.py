## requirments : pip install pyttsx3 pywin32

## code
import pyttsx3

usinp = input("Enter the text you want to convert to speech: ")

engine = pyttsx3.init()
engine.say(usinp)
engine.runAndWait()
