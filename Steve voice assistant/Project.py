# import playsound
#
# playsound.playsound("info.mp3", True)

import playsound
import speech_recognition as sr
import pyautogui as pys


def start():
    global r, audio
    r = sr.Recognizer()
    # my_mic = sr.Microphone(device_index=1)
    with sr.Microphone() as source:
        print("Gapiring...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        listen()
    # print(r.recognize_google(audio))


def listen():
    try:
        say_now = r.recognize_google(audio, language="ru-RU")
        if 'Привет' in say_now:
            playsound.playsound('hello.mp3', True)
            # self()
            start()
        elif say_now == 'happy':
            playsound.playsound('year.mp3', True)
            # congratulations()
            start()
        elif say_now == 'info':
            playsound.playsound('info.mp3', True)
            # info()
            start()
        elif say_now == 'program':
            playsound.playsound('program.mp3', True)
            # program()
            write()
        elif say_now == 'music':
            playsound.playsound('The_Weeknd_Blinding_Lights_Lyrics_64_kbps_convertmp3_me.mp3', True)
            # play_music()
            start()

    except sr.UnknownValueError:
        return 'error'
    except sr.RequestError:
        return 'error'


# def self():
#     playsound.playsound('hello.mp3')
#
#
# def congratulations():
#     playsound.playsound('year.mp3')
#
#
# def info():
#     playsound.playsound('info.mp3')
#
#
# def program():
#     playsound.playsound('program.mp3')
#
#
# def play_music():
#     playsound.playsound('The_Weeknd_Blinding_Lights_Lyrics_64_kbps_convertmp3_me.mp3')


def write():
    pys.hotkey('ctrl', 'tab')
    pys.typewrite('''
import turtle

import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)

n = 90
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1 / n
    t.color(c)
    t.circle(180)
    t.left(10)
    ''', 0.05)
    pys.hotkey('ctrl', 'alt', 'l')
    pys.hotkey('ctrl', 'shift', 'f10')


start()
