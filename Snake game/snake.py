import turtle

POST = [(0, 0), (-20, 0), (-40, 0)]
from turtle import Turtle
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in POST:
            self.add_seg(position)

    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]



    def move(self):
        for t in range(len(self.segments) - 1, 0, -1):
            x = self.segments[t - 1].xcor()
            y = self.segments[t - 1].ycor()
            self.segments[t].goto(x, y)
        self.head.forward(20)

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def add_seg(self,position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


