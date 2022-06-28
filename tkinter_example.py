import tkinter as tk
import random
from colorutils import random_web


def color_gen(width_line, height_line, n):
    """
    Функция генерирует цветные полосы со случайными цветами
    :param width_line: ширина полосы
    :param height_line: высота полосы
    :param n: количество полос
    :return:
    """
    window = tk.Tk()
    for i in range(0, n):
        rn = random_web()
        frame = tk.Frame(master=window, width=width_line, height=height_line, bg=rn)
        frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        frame = tk.Frame(master=window, width=width_line, height=height_line, bg=rn)
        frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        frame = tk.Frame(master=window, width=width_line, height=height_line, bg=rn)
        frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
        frame = tk.Frame(master=window, width=width_line, height=height_line, bg=rn)
        frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    window.mainloop()


def test_monitor(width_line, height_line):
    """
    Функция генерирует тест монитора
    :param width_line: ширина полосы
    :param height_line: высота полосы
    :return:
    """
    rainbow_line = ['white', 'yellow', 'aqua', 'green', 'magenta', 'red', 'blue', 'black']
    # color_line = ['#FFFFFF', '#FFFF00', '#00FFFF', '#008000', '#800080', '#0000FF', '#000000']
    random.shuffle(rainbow_line)
    window = tk.Tk()
    for i in rainbow_line:
        frame = tk.Frame(master=window, width=width_line, height=height_line, bg=i)
        frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    window.mainloop()


def gradient(width_line, height_line):

    color_line1 = ['#000000', '#100000', '#200000', '#300000', '#400000', '#500000', '#600000', '#700000']
    color_line2 = ['#000000', '#000010', '#000020', '#000030', '#000040', '#000050', '#000060', '#000070']
    color_line3 = ['#00000A', '#00000B', '#00000C', '#00000D', '#00000F', '#000000', '#000000', '#000000']
    color_line4 = ['#000000', '#001000', '#002000', '#003000', '#004000', '#005000', '#006000', '#007000']
    color_line5 = ['#000000', '#010000', '#020000', '#030000', '#040000', '#050000', '#060000', '#070000']
    color_line6 = ['#100000', '#200000', '#300000', '#400000', '#500000', '#600000', '#700000', '#700000']
    color_line7 = ['#00000', '#00000', '#00000', '#00000', '#00000', '#00000', '#00000', '#00000']
    # random.shuffle(rainbow_line)
    window = tk.Tk()
    for i in color_line1:
        frame = tk.Frame(master=window, width=width_line, height=height_line, bg=i)
        frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    for i in color_line2:
        frame = tk.Frame(master=window, width=width_line, height=height_line, bg=i)
        frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    for i in color_line3:
        frame = tk.Frame(master=window, width=width_line, height=height_line, bg=i)
        frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    for i in color_line4:
        frame = tk.Frame(master=window, width=width_line, height=height_line, bg=i)
        frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    window.mainloop()


def gradient1(width_line, height_line, n):

    start_color = 0  # начальное значение цвета
    window = tk.Tk()
    for i in range(0, n):
        start_color += 4096  # шаг изменения цвета
        clr = str('#' + str(start_color).zfill(6))  # создание нового цвета заполнение нулями до 6 символов
        frame = tk.Frame(master=window, width=width_line, height=height_line, bg=clr)
        frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    window.mainloop()


if __name__ == "__main__":
    # color_gen(20, 20, 50)
    # test_monitor(220, 1000)
    # gradient(50, 100)
    gradient1(10, 1000, 200)

