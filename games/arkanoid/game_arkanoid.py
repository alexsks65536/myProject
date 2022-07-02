"""
Игра "Арканоид"
pip install pgzero
"""

import pgzrun
from pgzero import screen
from pgzero.actor import Actor


def draw():
    # screen.blit("background.png", (0,0))
    paddle.draw()
    ball.draw()


def update():
    pass


TITLE = "Arkanoid clone"
WIDTH = 800
HEIGHT = 500

paddle = Actor("paddleblue.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ballblue.png")
ball.x = 30
ball.y = 300

pgzrun.go()