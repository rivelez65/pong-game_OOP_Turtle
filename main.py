from turtle import Screen
from scoreboard import Scoreboard
from paddles import Paddles
from pong import Pong
import time

game_is_on = True

screen = Screen()
screen.tracer(0)
screen.update()

pad = Paddles()
screen.setup(800, 600)
screen.title("THE PONG GAME")

screen.listen()
screen.bgcolor("black")
scoreboard = Scoreboard()

screen.onkey(key='w', fun=pad.move_up_1)
screen.onkey(key='s', fun=pad.move_down_1)
screen.onkey(key='Up', fun=pad.move_up_2)
screen.onkey(key='Down', fun=pad.move_down_2)

scoreboard.draw_walls()
pong = Pong()
screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.05)
    pong.move()

    if pong.ball.ycor() > 260 or pong.ball.ycor() < -260:
        pong.bounce()

    if pong.ball.xcor() > 320 and pong.ball.distance(pad.t_2) < 50:
        pong.hit()
        pong.move()

    if pong.ball.xcor() > 380:
        scoreboard.player_1_scores()
        scoreboard.update_score()
        pong.ball.goto(0, 0)

    if pong.ball.xcor() < -320 and pong.ball.distance(pad.t_1) < 50:
        pong.hit()

    if pong.ball.xcor() < -380:
        scoreboard.player_2_scores()
        scoreboard.update_score()
        pong.ball.goto(0, 0)

screen.exitonclick()
