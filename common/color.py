def switch_color(color):
    """
    Функция принимает в качестве аргумента цвет,
    возвращает код цвета, если аргумент неверный,
    выдает код белого цвета
    :param color:
    :return:
    """
    color = color.lower()
    switcher = {
        'black': '[30m',
        'red': '[31m',
        'green': '[32m',
        'yellow': '[33m',
        'blue': '[34m',
        'purple': '[35m',
        'lightblue': '[36m',
        'white': '[37m',
    }
    return switcher.get(color, '[37m')


def switch_background(color):
    color = color.lower()
    switcher = {
        'black': '[40m',
        'red': '[41m',
        'green': '[42m',
        'yellow': '[44m',
        'blue': '[44m',
        'purple': '[45m',
        'lightblue': '[46m',
        'white': '[47m',
    }
    return switcher.get(color, '')


def switch_effect(color):
    color = color.lower()
    switcher = {
        'reset': '[0m',
        'bold': '[1m',
        'fade': '[2m',
        'italic': '[3m',
        'underlined': '[4m',
        'flash': '[5m',
        'flasher': '[6m',
        'changeback': '[7m',
    }
    return switcher.get(color, '')


if __name__ == "__main":
    color_line = ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'lightblue', 'white']
    for i in color_line:
        col = switch_color(i)
        print(f'\033{col}########')
