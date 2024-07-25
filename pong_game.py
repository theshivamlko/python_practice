from turtle import Screen , Turtle
# import sys
# print(sys.path)

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)


paddle =Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.penup()
paddle.goto(350,0)


def go_up():
    newY=paddle.ycor()+20
    paddle.goto(paddle.xcor(),newY)

def go_down():
    newY=paddle.ycor()-20
    paddle.goto(paddle.xcor(),newY)

screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

screen.exitonclick()