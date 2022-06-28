import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file():
    """Открывает файл для редактирования"""
    # используют диалоговое окно askopenfilename из модуля tkinter.filedialog, чтобы отобразить диалоговое окно
    # открытия файла и сохранить выбранный путь к файлу в переменную filepath;
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    # проверяют, закрывает ли пользователь диалоговое окно или нажимает кнопку отмены. Если это так, то filepath будет
    # иметь значение None, и функция вернется без выполнения какого-либо кода для чтения содержимого файла и вставки
    # текста в текстовом поле txt_edit;
    if not filepath:
        return
    # очищает текущее содержимое из текстового поля txt_edit, используя метод .delete();
    txt_edit.delete("1.0", tk.END)
    # открывают выбранный файл и читают через .read() его содержимое перед сохранением текста в виде строки;
    with open(filepath, "r", encoding='utf-8') as input_file:
        text = input_file.read()
        # вставляем текст в текстовом поле txt_edit, используя метод .insert();
        txt_edit.insert(tk.END, text)
    #     устанавливает заголовок окна так, чтобы он содержал путь к открытому файлу.
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    """Сохраняем текущий файл как новый файл."""
    # используют диалоговое окно asksaveasfilename, чтобы выбрать желаемое место сохранения файла.
    # Выбранный путь к файлу сохраняется в переменную filepath;
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
    )
    # проверяют, закрывает ли пользователь диалоговое окно или нажимает кнопку отмены. Если это так, то переменная
    # filepath будет иметь значение None, и функция завершиться без выполнения какого-либо кода для сохранения
    # текста в файле;
    if not filepath:
        return
    # создает новый файл по выбранному пути;
    with open(filepath, "w", encoding='utf-8') as output_file:
        # извлекает текст из текстового поля txt_edit с помощью метода .get() и присваивает его переменной text;
        text = txt_edit.get("1.0", tk.END)
        # записывает содержимое из переменной text в выбранном файле;
        output_file.write(text)
    #     обновляет заголовок окна приложения, чтобы новый путь к файлу отображался в заголовке окна.
    window.title(f"Простой текстовый редактор - {filepath}")


window = tk.Tk()
window.title("Простой текстовый редактор")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text="Открыть", command=open_file)
btn_save = tk.Button(fr_buttons, text="Сохранить как...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
