"""
    Функция принимает в качестве аргументы номер месяца,
    печатает название месяца, если аргумент неверный,
    выдает "Invalid month"
"""


def switch_demo(argument):
    switcher = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    print(switcher.get(argument, 'Invalid month'))


for i in range(1, 13):
    switch_demo(i)
