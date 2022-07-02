from tkinter import Tk, Canvas, Frame, BOTH
from colorutils import random_web
import random


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Рисуем формы")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        dim = 200
        0  # задаем диаметр круга
        y_quan = 1024 // dim  # определяем кол-во кругов по вертикали
        x_quan = 1920 // dim  # определяем кол-во кругов по горизонтали
        print(f'Кол-во кругов по горизонтали: {x_quan}\nКол-во кругов по вертикали: {y_quan}')
        for y in range(0, y_quan):  # создаем цикл вычисления координат по вертикали
            for x in range(0, x_quan):  # создаем цикл вычисления координат по горизонтали
                r_fill = random_web()  # получаем случайный цвет заполнения фигуры
                r_out = random_web()  # получаем случайный цвет контура фигуры
                canvas.create_oval(
                    x * dim, y * dim, x * dim + dim, y * dim + dim,
                    outline=r_out,
                    fill=r_fill,
                    width=1
                )
                n1 = dim // 2
                for n in range(0, n1, 10):  # Создаем внутренние концентрические круги
                    r_fill = random_web()  # получаем случайный цвет заполнения фигуры
                    r_out = random_web()  # получаем случайный цвет контура фигуры
                    canvas.create_oval(
                        x * dim + n, y * dim + n, x * dim + dim - n, y * dim + dim - n,
                        outline=r_out,
                        fill=r_fill,
                        width=1
                    )
        canvas.pack(fill=BOTH, expand=1)


def main():
    h_win = 1920  # ширина окна
    v_win = 1024  # высота окна
    root = Tk()
    ex = Example()
    root.geometry(f"{h_win}x{v_win}")  # размер окна
    root.mainloop()


if __name__ == '__main__':
    main()
