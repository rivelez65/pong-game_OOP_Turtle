from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 40, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.color('blue')
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score_1}     {self.score_2}", align=ALIGNMENT, font=FONT)

    def player_1_scores(self):
        self.clear()
        self.score_1 += 1
        self.update_score()

    def player_2_scores(self):
        self.clear()
        self.score_2 += 1
        self.update_score()

    def draw_walls(self):
        t = Turtle()
        t.penup()
        t.color("black")
        t.pencolor('white')
        t.speed('fastest')
        t.pensize(5)
        t.goto(0, 300)
        t.setheading(270)
        t.pendown()
        for x in range(25):
            t.forward(10)
            t.penup()
            t.forward(20)
            t.pendown()
