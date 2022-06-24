import tkinter as tk
import random


window = tk.Tk()
width_line = 100  # ширина полосы
height_line = 1000  # высота полосы
rainbow_line = ['white', 'yellow', 'aqua', 'green', 'magenta', 'red', 'blue', 'black']
color_line = ['#FFFFFF', '#FFFF00', '#00FFFF', '#008000', '#800080', '#0000FF', '#000000']
color_raw = hex(range(0x000000, 0x0000FF))
color("#%06x" % random.randint(0, 0xFFFFFF))
print(hex(255))
print(color_raw)
# random.shuffle(rainbow_line)
for i in color_line:
    frame = tk.Frame(master=window, width=width_line, height=height_line, bg=i)
    frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
