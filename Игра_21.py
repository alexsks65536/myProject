import tkinter as tk
import random

window = tk.Tk()
# # параметры виджета
# greeting = tk.Label(
#     text="Привет, Tkinter!",
#     foreground="white",  # Устанавливает белый текст
#     background="#34A2FE",  # Устанавливает фон
#     width=20,  # ширина ярлыка
#     height=10  # высота ярлыка
#     )
# # параметры кнопки
# button = tk.Button(
#     text="Нажми на меня!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="red",
# )
# entry = tk.Entry(fg="yellow", bg="blue", width=50)  # Виджет Entry — Однострочное текстовое поле
# entry.insert(0, "Иванов")  # можете вставить текст в виджете однострочного текстового поля с помощью метода
# entry.insert(0, "Иван ")  # вставили следующее значение
#  name = entry.get()
#  entry.delete(0)
# создаем текстовый виджет
text_box = tk.Text()
text_box.pack()
#
text_box.get("1.0")
# greeting.pack()
# entry.pack()
# button.pack()
window.mainloop()


