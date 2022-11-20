from turtle import *
FONT=("Courier",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.goto(-280,250)
        self.updateboard()

    def updateboard(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def increaselevel(self):
        self.level+=1
        self.updateboard()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
