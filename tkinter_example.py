import tkinter as tk
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
    # rainbow_line = ['white', 'yellow', 'aqua', 'green', 'magenta', 'red', 'blue', 'black']
    # color_line = ['#FFFFFF', '#FFFF00', '#00FFFF', '#008000', '#800080', '#0000FF', '#000000']

    # random.shuffle(rainbow_line)

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


if __name__ == "__main__":
    color_gen(20, 20, 50)
