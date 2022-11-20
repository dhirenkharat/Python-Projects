from turtle import *
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        with open("data.txt",mode="r") as file:
            self.highscore = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.highscore}" , align="center",font=("Arial",20,"normal"))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score=0
        self.update()

    def inc_score(self):
        self.score+=1
        self.clear()
        self.update()
