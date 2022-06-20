from common.utils import Separator  # импортируем класс

sep1 = Separator()  # создаем экземпляр класса
sep1.make_separator('gray', 'black', 60, '-', 'bold', 'Новый параграф')


def get_vowels(String):
    """
    Этот пример возвращает в строке найденные гласные "a e i o u".
    :param String:
    :return:
    """
    return [each for each in String if each in "aeiou"]


print(get_vowels("animal"))  # [a, i, a]
print(get_vowels("sky"))  # []
print(get_vowels("football"))  # [o, o, a]

sep1.make_separator('gray', 'black', 60, '-', 'bold', 'Интерпретатор hq9+')

###########################################################################
# вводим имя файла example.txt
f = open(input('Enter file name: '))
s = f.read()
f.close()
template = '''{} bottles of beer on the wall.
Take one down and pass it around, {} bottles of beer on the wall.'''
count = 0  # Никому не нужный счётчик

for i in s.upper():  # Игнорируем регистр
    if i == 'H':
        print('Hello, world!')  # Выводим 'Hello, world!'
    elif i == 'Q':
        print(s)  # Выводим саму программу
    elif i == '9':
        for i in range(99, 1, -1):
            print(template.format(i, i-1))  # Выводим текст песни
        print('1 bottle of beer on the wall.\nTake one down and pass it around, no more bottles of beer on the wall.')
        print('No more bottles of beer on the wall.\nGo to the store and buy some more, 99 bottles of beer on the wall.')
    elif i == '+':
        count += 1