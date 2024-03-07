from gtts import gTTS
import playsound
def sum(text1):
    tts = gTTS(text="Hello, {a}!".format(a="karan"), lang='en')
    tts.save("hello.mp3")
    playsound.playsound("hello.mp3")

import speech_recognition as sr
text1="attendance marked"
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_google(audio)
#a = "karan"
if(text=="hello"):
    sum(text1)        