import pyttsx3
import gtts
import docx
import pyaudio
import speech_recognition as sr
import os
import sys
import webbrowser
import googletrans
from googletrans import Translator

translator = Translator()




def talk(words):
    print(words) # Дополнительно выводим на экран
    os.system("say " + words)

talk('Скажи, и я переведу')

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Говорите')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio, language='ru-RU').lower()

        print(zadanie)

    except sr.UnknownValueError:
        talk('Я не понимаю')
        zadanie = command()

    return zadanie


def makeSomething(zadanie):    
    result = translator.translate(zadanie, src='ru', dest='en')
    voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.9)
    engine.setProperty('voice', voice_id)

    if zadanie: 
        engine.say(result.text)
        print(result.text)

    engine.runAndWait()

    rus_en = []
    rus_en.append(zadanie)
    rus_en.append(result.text)
    print(rus_en)
    return rus_en

def translateText(text_translate):    
    text_result = translator.translate(text_translate, src='ru', dest='en')

    return text_result.text
        

