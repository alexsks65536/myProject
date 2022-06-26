import tkinter as tk  # Импортируем библиотеку tkinter и назначаем имя "tk"


# Окно, или window является экземпляром класса Tkinter
window = tk.Tk()
#  Создадим виджет ярлыка (label) с текстом "Привет, Tkinter!" и присвоим его переменной под названием greeting:
greeting = tk.Label(
    text="Привет, Tkinter!",
    foreground="white",  # Устанавливает белый текст
    background="black",  # Устанавливает черный фон
    width=20,  # Ширина окна, измеряется в текстовых юнитах
    height=20  # Высота окна
)
# создаем кнопку с синим фоном и желтым текстом
button = tk.Button(
    text="Нажми на меня!",
    width=20,
    height=3,
    bg="blue",
    fg="yellow",
)
#  Виджет Entry — Однострочное текстовое поле
entry = tk.Entry(fg="yellow", bg="SkyBlue1", width=50)
#  Виджет Text — ввод большого текста в Tkinter
text_box = tk.Text()
# можете вставить текст в текстовый виджет с помощью метода  .insert():
text_box.insert("1.0", "Hello")
# вставляем вторую строчку
text_box.insert("2.0", "\nWorld")
text_box.insert(tk.END, "Вставь меня в самом конце!")
text_box.insert(tk.END, "\nВставь меня в новую строку!")
# Для получения всего текста из текстового виджета установите индекс на "1.0" и
# используйте специальную константу tk.END для второго индекса:
print(f'В текстовое поле введено: {text_box.get("1.0", tk.END)}')
# while True:
#     a = input('Введите: ')
#     if a == 'q':
#         break

#  можно использовать метод .pack() для добавления виджета на окно
greeting.pack()  # Запуск виджета label
button.pack()  # Запуск виджета button
entry.pack()  # Запуск виджета entry
text_box.pack()  # Запуск виджета text_box
#  запустить цикл событий Tkinter
window.mainloop()


