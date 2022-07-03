"""
Игра "Арканоид"
pip install pgzero
"""
import random

import pgzrun
from pgzero import screen
from pgzero.actor import Actor
from pgzero.keyboard import keyboard

bars_list = []
ball_x_speed = 1
ball_y_speed = 1



def draw():
    screen.blit("background.png", (0, 0))
    paddle.draw()
    ball.draw()
    for bar in bars_list:
        bar.draw()


def place_bars(x, y, image):
    bar_x = x
    bar_y = y
    for i in range(8):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)


def update():
    global ball_x_speed, ball_y_speed
    update_ball()
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1
    if keyboard.left:
        paddle.x = paddle.x - 5
    if keyboard.right:
        paddle.x = paddle.x + 5
    if paddle.colliderect(ball):
        ball_y_speed *= -1
        # randomly move ball left or right on hit
        rand = random.randint(0, 1)
        if rand:
            ball_x_speed *= -1


def update_ball():
    ball_move_x = 1
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH) or (ball.x <= 0):  # Если x превышает максимальное значение WIDTH, которое мы определили для
        # игры (то есть мяч выходит за правую часть экрана), или меньше 0 (то есть выходит за левую часть экрана)
        ball_x_speed *= -1
    if (ball.y >= HEIGHT) or (ball.y <= 0):
        ball_y_speed *= -1
    rand = random.randint(0, 1)
    if rand:
        ball_move_x *= -1


TITLE = "Arkanoid clone"
WIDTH = 800
HEIGHT = 500

paddle = Actor("paddleblue.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ballblue.png")
ball.x = 30
ball.y = 300

bar = Actor("element_blue_rectangle_glossy.png")
bar.x = 120
bar.y = 100

coloured_box_list = \
    ["element_blue_rectangle_glossy.png",
     "element_green_rectangle_glossy.png",
     "element_red_rectangle_glossy.png"]
x = 120
y = 100
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50

pgzrun.go()
