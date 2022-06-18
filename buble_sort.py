import random
import numpy as np


def bSort(array):
    """
    Сортировка пузырьком
    :param array: исходный массив
    :return: отсортированный массив
    """
    # определяем длину массива
    length = len(array)
    # Внешний цикл, количество проходов N-1
    for i in range(length):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, length - i - 1):
            # Меняем элементы местами
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


# a = [3, 1, 6, 4, 8, 54, 69, 29, 69]
lst = np.random.randint(0, 1000, 1000)
bSort(lst)
print(lst)
