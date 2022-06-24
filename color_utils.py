from colorutils import random_web
from tkinter import Tk, Button

mgui = Tk()
mgui.geometry('150x28+400+200')


def rcolor():
    rn = random_web()
    print(rn)  # for terminal watchers
    cbutton.config(text=rn)
    mgui.config(bg=rn)


cbutton = Button(text="Click", command=rcolor)
cbutton.pack()

mgui.mainloop()
