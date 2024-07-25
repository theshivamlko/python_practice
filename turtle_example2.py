from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()


def moveForward():
    tim.forward(20)
def moveBack():
    tim.back(20)
def turnLeft():
    tim.left(90)
def turnRight():
    tim.right(90)

screen.listen()

screen.onkey(key="Right",fun=moveForward)
screen.onkey(key="Left",fun=moveBack)
screen.onkey(key="Up",fun=turnLeft)
screen.exitonclick()