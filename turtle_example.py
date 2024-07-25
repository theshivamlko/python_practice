from turtle import Turtle,Screen
# from turtle import Turtle,Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("#FF0000")

for i in range(6):
    timmy.forward(100)
    timmy.left(60)


screen = Screen()
screen.exitonclick()