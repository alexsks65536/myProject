import tkinter as tk
import random

window = tk.Tk()
greeting = tk.Label(
    text="Привет, Tkinter!",
    foreground="white",  # Устанавливает белый текст
    background="#34A2FE",  # Устанавливает фон
    width=20,  # ширина ярлыка
    height=10  # высота ярлыка
    )
button = tk.Button(
    text="Нажми на меня!",
    width=25,
    height=5,
    bg="blue",
    fg="red",
)
entry = tk.Entry(fg="yellow", bg="blue", width=50)  # Виджет Entry — Однострочное текстовое поле
#  name = entry.get()
#  entry.delete(0)
greeting.pack()
entry.pack()
button.pack()
window.mainloop()


