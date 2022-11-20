from turtle import Turtle
STARTING_POSITION=(0,-280)
MOVE=10
FINISH_LINE=280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.gotostart()
        self.shape("turtle")
        self.setheading(90)

    def goup(self):
        self.forward(MOVE)

    def gotostart(self):
        self.goto(STARTING_POSITION)

    def isfinish(self):
        if self.ycor()>FINISH_LINE:
            return True
        else:
            return False

