from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

final_score = int(screen.textinput("Final Score", "Enter the final score of the game"))

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

score_board = Scoreboard()

game_on = True
speed = 0.15
while game_on:
    screen.update()
    ball.move()
    time.sleep(speed)

    # detect walls collision
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.y_move *= -1

    # detect paddles collision
    if (ball.distance(l_paddle) < 50 and ball.xcor() < -320) \
            or (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.x_move *= -1
        if speed > 0:
            speed -= 0.005

    # detect when out of bounce
    if ball.xcor() > 390:
        ball.goto(0, 0)
        score_board.update_l_score()
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        score_board.update_r_score()

    if score_board.l_score == final_score or score_board.r_score == final_score:
        game_on = False
        score_board.game_over()

screen.exitonclick()
