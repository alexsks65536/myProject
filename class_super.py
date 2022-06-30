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

        # Овальная форма.
        color = "#f11"

        for i in range(0, 10):
            r_fill = random_web()
            r_out = random_web()
            x_coord = random.randint(5, 1000)
            y_coord = random.randint(5, 1000)
            canvas.create_oval(
                x_coord, x_coord, x_coord+30, x_coord+30, outline=r_out,
                fill=r_fill, width=2
            )

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("1900x1000")
    root.mainloop()


if __name__ == '__main__':
    main()