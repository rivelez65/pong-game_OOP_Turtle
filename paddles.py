from turtle import Turtle
MOVE = 40


class Paddles:

    def __init__(self):
        self.t_1 = Turtle()
        self.t_1.shape('square')
        self.t_1.color('white')
        self.t_1.speed('fastest')
        self.t_1.penup()
        self.t_1.shapesize(1, 5)
        self.t_1.goto(-350, 0)
        self.t_2 = Turtle()
        self.t_2.shape('square')
        self.t_2.color('white')
        self.t_2.penup()
        self.t_2.speed('fastest')
        self.t_2.shapesize(1, 5)
        self.t_2.goto(350, 0)
        self.t_1.seth(90)
        self.t_2.seth(90)
        self.pad_1 = self.t_1.ycor()
        self.pad_2 = self.t_2.ycor()

    def move_up_1(self):
        self.t_1.forward(MOVE)

    def move_down_1(self):
        self.t_1.backward(MOVE)

    def move_up_2(self):
        self.t_2.forward(MOVE)

    def move_down_2(self):
        self.t_2.backward(MOVE)
