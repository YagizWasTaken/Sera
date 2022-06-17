from asyncore import write
import imp
from urllib import response
from playsound import  playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import date, datetime
import random
from random import choice
import webbrowser
import tkinter as tk
import requests
import time
from yeelight import Bulb




r = sr.Recognizer()



def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Sera- Anlayamadım, lütfen tekrar eder misiniz?")
            speak("Anlayamadım")
        except sr.RequestError:
            print("Sera- Sistem çalışmıyor")
        return voice


def response(voice):
    if "sera" in voice:
        speak ("efendim")
    if "merhaba" in voice:
        speak("merhaba")
    if  "selam" in voice:
        speak("sana da selam")
    if "nasılsın" in voice:
        speak("gayet iyi bir şekilde çalışıyorum, sen nasılsın")
    if "iyiyim" in voice or "fena değil" in voice:
        speak("bunu duyduğuma sevindim")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")
    if "görüşürüz" in voice or "uyu" in voice or "kapan" in voice:
        speak("görüşürüz efendim")
        exit()
    if "yeniden başla" in voice:
        speak("yeniden başlatma işlemi bu sistem için uygun değil.isterseniz kapanabilirim.")
    if "sen kimsin" in voice or "nesin sen" in voice:
        speak("Ben sera.Yağız Arslanın geliştirdiği özel bir yazılımım.Amacım Yağız Arslan ve yakınlarına yardımcı olmak.Senin için ne yapabilirim?")
    if "alo" in voice or "sesim geliyor mu" in voice or "deneme" in voice:
        speak("Sesiniz gayet güzel bir şekilde geliyor efendim.")
    if "hangi gündeyiz" in voice or "bugün ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"
        
        print(today)
        speak(today)


    if "saat" in voice:
        selection = ["Saat şu an: ", "Hemen bakıyorum: "]
        clock = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        print(selection + clock)
        speak(selection + clock)

    if "zar at" in voice or "sayı söyle" in voice:
        zar = ["1","2","3","4","5","6"]
        zar = random.choice(zar)
        print(zar)
        speak(zar)

       
    
    if "google'da ara" in voice or "web'de ara" in voice:
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} için Google'da bulabildiklerimi listeliyorum.".format(search))
    
    if "youtube'da ara" in voice:
        speak("Ne aramamı istersin?")
        search = record()
        url = "https://www.youtube.com//search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} için youtube'de bulabildiklerimi listeliyorum.".format(search))
    
    if "müzik çal" in voice or "şarkı aç" in voice or "müzik aç" in voice:
        speak("hemen açıyorum")
        
        url = "https://music.youtube.com/watch?v=wRE8SW0HVvk&list=PL4vm_vHHJfhifRECp5udgVjCIM3XlUcJy"
        webbrowser.get().open(url)
        speak("Engelbert Humperdinck'den A Man Without Love çalıyor")

    if "müzik listemi aç" in voice or "şarkı listemi aç" in voice:
        speak("hemen açıyorum")
        
        url = "https://music.youtube.com/playlist?list=PL4vm_vHHJfhifRECp5udgVjCIM3XlUcJy"
        webbrowser.get().open(url)
        speak("favori şarkılarınız açıldı")
    
    
    if "aydınlat beni" in voice:
        bulb=Bulb("192.168.1.46")
        bulb.turn_on()
        speak("Işık açıldı")
    
    if "etrafı karart" in voice or "ışığı kapat" in voice or "karanlık" in voice:
        bulb=Bulb("192.168.1.46")
        bulb.turn_off()
        speak("ışık kapatıldı")
    
    if "renk mavi olsun" in voice:
        bulb=Bulb("192.168.1.46")
        bulb.set_rgb(0, 0, 255)
        speak("Işık rengi maviye değiştirildi.")






def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
   

   



print("Sera etkin durumda.")
print("Yağız Arslan'a hizmet etmek için hazır.")
speak("hizmetinizdeyim efendim, size nasıl yardımcı olabilirim?")


while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice)
        response(voice)








