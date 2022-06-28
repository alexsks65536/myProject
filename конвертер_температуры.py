import tkinter as tk


def fahrenheit_to_celsius():
    """
    Конвертирует значение Фаренгейта в Цельсий и вставляет
    результат в ярлык lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


window = tk.Tk()
window.title("Конвертер температуры")  # устанавливает заголовок для существующего окна
frm_entry = tk.Frame(master=window)  # создаем рамку
ent_temperature = tk.Entry(master=frm_entry, width=10)  # создаем виджет однострочного текстового поля
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")  # создаем ярлык и вставляем в рамку frm_entry
ent_temperature.grid(row=0, column=0, sticky="e")  # установили параметр sticky на "e" для текстового поля
# ent_temperature таким образом, чтобы она всегда будет с правой стороны ячейки сетки.
lbl_temp.grid(row=0, column=1, sticky="w")  # Также установили sticky на "w" для ярлыка  lbl_temp для закрепления с
# левой стороны его ячейки сетки.
# Теперь заставим кнопку btn_convert и ярлык с результатом lbl_result конвертировать введенную в текстовом поле
# ent_temperature температуру, после чего отобразить результат на экране
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
# Используем метод .grid(), чтобы разместить их должным образом
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
window.mainloop()
