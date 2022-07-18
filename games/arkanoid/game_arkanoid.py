"""
Игра "Арканоид"
pip install pgzero
"""
import random
import pgzrun


TITLE = "Arkanoid clone"
WIDTH = 1920  # задаем размеры игрового поля
HEIGHT = 1078

paddle = Actor("paddleblue.png")
paddle.x = 120  # задаем начальное положение ракетки
paddle.y = 850

y_level = HEIGHT - paddle.y + 10  # уровень отскока мяча от нижнего края поля = высота окна - положение ракетки + 10

ball = Actor("ballblue.png")
ball.x = 100  # начальное положение мяча
ball.y = 800

ball_x_speed = -5  # скорость перемещения мяча
ball_y_speed = -5

bars_list = []


def draw():
    screen.blit("background.png", (0,0))  # отображение фона
    paddle.draw()  # отображение ракетки
    ball.draw()  # отображение мяча
    for bar in bars_list:
        bar.draw()  # отображение блоков


def place_bars(x, y, image):  # функция отрисовывает блоки
    bar_x = x
    bar_y = y
    for i in range(25):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)


def update():
    global ball_x_speed, ball_y_speed
    if keyboard.left:  # если нажата кнопка клавиатуры влево
        paddle.x = paddle.x - 10  # скорость перемещения ракетки
    if keyboard.right:  # если нажата кнопка клавиатуры вправо
        paddle.x = paddle.x + 10

    update_ball(y_level)
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1

    if paddle.colliderect(ball):
        ball_y_speed *= -1
        # randomly move ball left or right on hit
        rand = random.randint(0, 1)
        if rand:
            ball_x_speed *= -1


def update_ball(y_level):
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH) or (ball.x <= 0):  # Если x превышает максимальное значение WIDTH, которое мы определили для
        # игры (то есть мяч выходит за правую часть экрана), или меньше 0 (то есть выходит за левую часть экрана)
        ball_x_speed *= -1
    if (ball.y >= HEIGHT-y_level) or (ball.y <= 0):
        ball_y_speed *= -1
    # if (ball.y >= HEIGHT)


coloured_box_list = \
    ["element_green_rectangle_glossy.png",
     "element_blue_rectangle_glossy.png",
     "element_green_rectangle_glossy.png",
     "element_red_rectangle_glossy.png",
     "element_green_rectangle_glossy.png",
     "element_blue_rectangle_glossy.png",
     "element_green_rectangle_glossy.png",]
x = 120  # координаты начала отображения блоков
y = 100
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50

pgzrun.go()

