import os
from tkinter import *
import playsound
import webbrowser as wb
import speech_recognition as sr

root = Tk()


def btn_click():
    global r, audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            say_now = r.recognize_google(audio, language="ru-RU")
            print(say_now)
            if 'Стив' in say_now:
                playsound.playsound('hello.mp3', True)
            elif 'info' in say_now:
                playsound.playsound('steven.mp3', True)
            elif 'питон' in say_now:
                playsound.playsound('payton.mp3', True)
            elif 'дата' in say_now:
                playsound.playsound('data.mp3', True)
            elif 'видео' in say_now:
                wb.open('https://www.youtube.com/')
            elif 'музыка' in say_now:
                os.system('Blinding.mp3')
                # playsound.playsound('Blinding.mp3', True)
            elif 'февраль' in say_now:
                os.system('February.mp3')
                # playsound.playsound('February.mp3', True)
            elif 'грузин' in say_now:
                os.system('Gruzin.m4a')
            elif 'такой' in say_now:
                os.system('JONY.m4a')
            elif 'Куран' in say_now:
                os.system('Yasin.mp3')
            else:
                return label1.pack()



        except sr.UnknownValueError:
            return 'error'
        except sr.RequestError:
            return 'error'


root['bg'] = '#fafafa'
root.title('AI by im')
root.iconbitmap(r'imai.ico')
root.wm_attributes('-alpha', 0.8)
root.geometry('350x550')
root.resizable(width=False, height=False)

bg = PhotoImage(file='design.png')
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

label1 = Label(root, text='Chunmadim!')

btn = Button(text='   Steve   ', bg='#1d2225', # #a276f9
             activebackground='#231a26',
             command=btn_click, padx=15, pady=10)
btn.place(x=130, y=490)

root.mainloop()











