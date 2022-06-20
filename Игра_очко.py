import random
from common.utils import Separator  # импортируем класс

sep1 = Separator()  # создаем экземпляр класса
sep1.make_separator('green', 'black', 60, '-', 'bold', 'Игра "Очко"')

koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(koloda)

print('Поиграем в "очко"?')
count = 0

while True:
    choice = input('Будете брать карту? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print(f'Вам попалась карта достоинством {current}')
        count += current
        if count > 21:
            print(f'\033[31m Извините, но вы проиграли\033[0m')
            break
        elif count == 21:
            print(f'\033[34m Поздравляю, вы набрали 21!\033[0m')
            break
        else:
            print(f'У вас {count} очков.')
    elif choice == 'n':
        print(f'У вас {count} очков и вы закончили игру.')
        break

print('До новых встреч!')
