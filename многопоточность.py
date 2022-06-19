import threading
import time
from common.utils import Separator


def myfunc(a, b):
    time.sleep(2.5)  # задержка в функции на 2.5 секунд
    print('сумма: ', a + b)


sep1 = Separator()
thr1 = threading.Thread(target=myfunc, args=(1, 2), daemon=True)
thr1.start()
thr1.join(0.125)  # После старта потока, мы приостанавливаем основной поток на 0.125 секунд
if thr1.is_alive():  # Выполняем проверку is_alive(). Если True, значит поток не закончил выполнение за 0.125 секунды.
    print('поток не успел завершиться')
else:
    print('вычисления завершены')

# =======================================================================
sep1.make_separator('gray', 'black', 120, '*', 'bold')


class Thr1(threading.Thread):  # Создаём экземпляр потока Thread
    def __init__(self, var):
        threading.Thread.__init__(self)
        self.daemon = True  # Указываем, что этот поток - демон
        self.var = var  # это интервал, передаваемый в качестве аргумента

    def run(self):  # метод, который выполняется при запуске потока
        num = 1
        while True:
            y = num*num + num / (num - 10)  # Вычисляем функцию
            num += 1
            print("При num =", num, " функция y =", y)  # Печатаем результат
            time.sleep(self.var)  # Ждём указанное количество секунд


x = Thr1(0.9)
x.start()
time.sleep(2)
