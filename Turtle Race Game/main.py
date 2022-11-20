from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
bet=screen.textinput("Make Your Bet","Which colour")

t1=Turtle()
t1.penup()
t1.setpos(-240,80)
t1.shape("turtle")
t1.color("red")

t2=Turtle()
t2.penup()
t2.setpos(-240,40)
t2.shape("turtle")
t2.color("blue")



t3=Turtle()
t3.penup()
t3.setpos(-240,0)
t3.shape("turtle")
t3.color("yellow")



t4=Turtle()
t4.penup()
t4.setpos(-240,-40)
t4.shape("turtle")
t4.color("green")



t5=Turtle()
t5.penup()
t5.setpos(-240,-80)
t5.shape("turtle")
t5.color("cyan")

a=random.randint(0,10)
b=random.randint(0,10)
c=random.randint(0,10)
d=random.randint(0,10)
e=random.randint(0,10)


flag=True


while flag:
    t1.forward(a)
    if t1.xcor()>=240:
        flag=False
        print("t1 won")
        if bet=="t1":
            print("You won the bet")
        else:
            print("Sorry You lost the best")
    t2.forward(b)
    if t2.xcor()>=240:
        flag=False
        print("t2 won")
        if bet=="t2":
            print("You won the bet")
        else:
            print("Sorry You lost the best")
    t3.forward(c)
    if t3.xcor()>=240:
        flag=False
        print("t3 won")
        if bet=="t3":
            print("You won the bet")
        else:
            print("Sorry You lost the best")
    t4.forward(d)
    if t4.xcor()>=240:
        flag=False
        print("t4 won")
        if bet=="t4":
            print("You won the bet")
        else:
            print("Sorry You lost the best")
    t5.forward(e)
    if t5.xcor()>=240:
        flag=False
        print("t5 won")
        if bet=="t5":
            print("You won the bet")
        else:
            print("Sorry You lost the best")




screen.exitonclick()