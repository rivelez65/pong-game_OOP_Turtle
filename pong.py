from turtle import Turtle
from random import randint


class Pong:

    def __init__(self):
        self.angle = randint(0, 90)
        self.ball = Turtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
        self.x_move = 7
        self.y_move = 7

    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
