from common.color import switch_color, switch_background, switch_effect
import random


class Separator:

    def make_separator(self, sep_color, sep_back, sep_num, sep_sym, sep_effect):
        color = switch_color(sep_color)
        back = switch_background(sep_back)
        effect = switch_effect(sep_effect)
        print(f'\033{color}\033{back}{sep_num * sep_sym}\033{effect}')


if __name__ == "__main__":
    sep1 = Separator()
    color_line = ['black', 'red', 'green', 'yellow', 'blue', 'purple', 'lightblue', 'white']
    random.shuffle(color_line)
    for i in color_line:
        color = switch_color(i)
        back = switch_background('none')
        effect = switch_effect('changeback')
        sep1.make_separator(color, back, 120, '@', effect)
