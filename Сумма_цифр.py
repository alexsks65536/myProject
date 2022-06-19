from common.utils import Separator  # импортируем класс

sep1 = Separator()  # создаем экземпляр класса
sep1.make_separator('gary', 'black', 100, '-', 'bold')


def sum_num(num):
    """
    Подсчет суммы цифр введенного числа
    :return: сумма
    """
    try:
        num = int(num)
        summ = 0
        while num != 0:
            summ = summ + num % 10
            num = num // 10
        return summ
    except:
        print(f'\033[31mВведено не целое число: {num}\033[0m')


def multi_num(num):
    try:
        num = int(num)
        mult = 1
        while num != 0:
            mult = mult * (num % 10)
            num = num // 10
        return mult
    except:
        print(f'\033[31mВведено не целое число: {num}\033[0m')


def multi_f():
    try:
        num = input("Введите дробное: ")
        # разделим введённое (тип данных строка) на две части
        x = num.split(".")
        a = int(x[0])  # целая часть
        b = int(x[1])  # дробная часть
        mult = 1
        while a != 0:  # перемножаем числа целой части
            mult = mult * (a % 10)
            a = a // 10
        while b != 0:  # перемножаем числа дробной части
            mult = mult * (b % 10)
            b = b // 10
        return mult
    except:
        print(f'\033[31mВведено не дробное число: {num}\033[0m')


num = input("Введите целое: ")
print(f'Сумма цифр числа равна:{sum_num(num)}')
sep1.make_separator('gary', 'black', 100, '+', 'bold')
print(f'Произведение цифр равно: {multi_num(num)}')
sep1.make_separator('gary', 'black', 100, '*', 'bold')
print(f'Произведение цифр равно: {multi_f()}')
sep1.make_separator('gary', 'black', 100, '=', 'bold')
