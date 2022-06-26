import tkinter as tk
from colorutils import random_web


window = tk.Tk()
width_line = 20  # ширина полосы
height_line = 1000  # высота полосы
# rainbow_line = ['white', 'yellow', 'aqua', 'green', 'magenta', 'red', 'blue', 'black']
# color_line = ['#FFFFFF', '#FFFF00', '#00FFFF', '#008000', '#800080', '#0000FF', '#000000']

# random.shuffle(rainbow_line)
for i in range(0, 255):
    rn = random_web()
    frame = tk.Frame(master=window, width=width_line, height=height_line, bg=rn)
    frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()
