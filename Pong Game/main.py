from turtle import Turtle,Screen
from paddle import Paddle
from ball import *
import time
from scoreboard import *


screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


padr=Paddle((350,0))
padl=Paddle((-350,0))
ball=Ball()
sc=Scoreboard()



screen.listen()

screen.onkey(padr.moveup,"Up")
screen.onkey(padr.movedown,"Down")
screen.onkey(padl.moveup,"w")
screen.onkey(padl.movedown,"s")

flag=True
flag2=True
while flag:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    if ball.distance(padr)<20 and ball.xcor()>320:
        ball.bounce_h()

    if ball.distance(padl)<20 and ball.xcor()<-320:
        ball.bounce_h()


    if ball.xcor()>380:
        ball.reset()
        sc.lpoint()

    if ball.xcor()<-380:
        ball.reset()
        sc.rpoint()





screen.exitonclick()