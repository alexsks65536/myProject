import random
from random import randint
from common.utils import Separator


sep1 = Separator()  # создаем экземпляр класса

sep1.make_separator('gray', 'black', 20, '-', 'bold', 'Вывод случайного числа при помощи использования random.random()')
print(random.random())
sep1.make_separator('green', 'black', 20, '-', 'bold', 'Вывод случайного целого числа')
print(randint(0, 9))
print(random.randrange(0, 10, 2))
sep1.make_separator('yellow', 'black', 20, '-', 'bold', 'Выбор случайного города из списка - ')
city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
print("", random.choice(city_list))
sep1.make_separator('blue', 'black', 20, '-', 'bold', 'Генерация случайного числа в пределах заданного промежутка')
print(random.randrange(10, 50, 5))
print(random.randrange(10, 50, 5))
sep1.make_separator('red', 'black', 20, '-', 'bold', 'random.choice используется для выбора случайного элемента из списка - ')
list = [55, 66, 77, 88, 99]
print("", random.choice(list))
sep1.make_separator('lightblue', 'black', 20, '-', 'bold', 'Генерация случайного числа в пределах заданного промежутка')
list = [2, 5, 8, 9, 12]
print("random.sample() ", random.sample(list, 3))
sep1.make_separator('white', 'black', 20, '-', 'bold', 'Случайное число с семенем ')
random.seed(6)
print("", random.random())
sep1.make_separator('green', 'black', 20, '-', 'bold', 'Вывод перемешанного списка ')
list = [2, 5, 8, 9, 12]
random.shuffle(list)
print(" ", list)
sep1.make_separator('blue', 'black', 20, '-', 'bold', 'Число с плавающей точкой в пределах заданного промежутка')
print(random.uniform(10.5, 25.5))
