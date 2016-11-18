import speech_recognition as sr
from gtts import gTTS
import os
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    # print("You said: " + r.recognize_google(audio))
    #print (r.recognize_google(audio))
    tts = gTTS(text=r.recognize_google(audio), lang='en')
    tts.save('hello.mp3')
    os.system('hello.mp3')
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))