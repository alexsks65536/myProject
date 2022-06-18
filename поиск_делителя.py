def delitel(numb):
    """
    Нахождение делителей числа.
    В цикле перебираются значения от делимого минус единица до двух включительно.
    Если делимое нацело делится на текущее значение, то оно является делителем.
    :param numb: 
    :return:
    """
    print("Результат:", end=" ")
    for i in range(numb - 1, 1, -1):
        if numb % i == 0:
            print(i, end=" ")


def simple_del(numb):
    """
    Простой делитель — это делитель, который делится только на единицу и самого себя
    :param numb:
    :return:
    """
    print("Простые:", end=" ")
    for i in range(numb - 1, 1, -1):
        is_simple = 0  # Счётчик
        if numb % i == 0:
            for j in range(i - 1, 1, -1):
                if i % j == 0:
                    is_simple = is_simple + 1  # Увеличиваем, если находим делитель
            if is_simple == 0:  # Если делителей не было найдено, выводим
                print(i, end=" ")


numb = int(input("Введите целое число: "))
# delitel(numb)  # поиск делителей
simple_del(numb)  # поиск простых делителей
