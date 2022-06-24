import tkinter as tk
from colorutils import random_web
import random


window = tk.Tk()
frame = tk.Frame(master=window, width=1000, height=1000)

frame.pack()

for i in range(0, 255):
    ix = random.randint(0, 1000)
    iy = random.randint(0, 1000)
    rn = random_web()
    label1 = tk.Label(master=frame, text="", width=1, height=1, bg=rn)
    label1.place(x=ix, y=iy)

window.mainloop()
