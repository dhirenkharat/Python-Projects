import time
from turtle import Turtle,Screen

from player import *
from car_manager import CarManager
from scoreboard import *

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player=Player()
cm=CarManager()
sc=Scoreboard()
screen.listen()
screen.onkey(player.goup,"Up")

flag=True
while flag:
    time.sleep(0.1)
    screen.update()
    cm.create_car()
    cm.move_cars()

    for car in cm.all_cars:
        if car.distance(player)<20:
            flag=False
            sc.gameover()

    if player.isfinish():
        player.gotostart()
        cm.levelup()
        sc.increaselevel()

screen.exitonclick()