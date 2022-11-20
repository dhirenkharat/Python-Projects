from turtle import Turtle,Screen
import time
from food import Food
from snake import Snake
from scoreboard import *
Score=0

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

s=Snake()
food=Food()
sb=Scoreboard()
screen.listen()
screen.onkey(s.up,"Up")
screen.onkey(s.down,"Down")
screen.onkey(s.left,"Left")
screen.onkey(s.right,"Right")

flag=True
while flag:
    screen.update()
    time.sleep(0.1)
    s.move()

    if s.head.distance(food)<15:
        food.refresh()
        sb.inc_score()
        s.extend()

    if s.head.xcor()>280 or s.head.xcor()<-280 or s.head.ycor()>280 or s.head.ycor()<-280:
        sb.reset()
        s.reset()
        print("Game Over")
    for seg in s.segments[1:]:
         if s.head.distance(seg)<10:
            sb.reset()
            s.reset()


screen.exitonclick()

