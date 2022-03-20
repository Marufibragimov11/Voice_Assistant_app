from tkinter import *
import playsound

root = Tk()


def btn_click():
    playsound.playsound("hello.mp3", True)


root['bg'] = '#fafafa'
root.title('AI by im')
root.wm_attributes('-alpha', 1)
root.geometry('300x480')
root.resizable(width=False, height=False)

bg = PhotoImage(file='background.png')
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

btn = Button(text='   Jarvis   ', bg='#a276f9',
             activebackground='blue',
             command=btn_click, padx=15, pady=10)
btn.pack(side=BOTTOM)

root.mainloop()