from turtle import *

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove=10
        self.ymove=10
        self.movespeed=0.1

    def move(self):
            m = self.xcor() + self.xmove
            n = self.ycor() + self.ymove
            self.goto(m, n)


    def bounce_y(self):
        self.ymove*=-1

    def bounce_h(self):
        self.xmove*=-1
        self.movespeed=self.movespeed*0.9

    def reset(self):
        self.goto(0,0)
        self.bounce_h()
