from turtle import *


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)


    def moveup(self):
        if self.ycor() < 240:
            new_x = self.xcor()
            new_y = self.ycor() + 20
            self.goto(new_x, new_y)

    def movedown(self):
        if self.ycor() > -240:
            new_x = self.xcor()
            new_y = self.ycor() - 20
            self.goto(new_x, new_y)
