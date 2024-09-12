from turtle import Screen , Turtle
from paddle_class import Paddle
from ball import Ball
import time

# import sys
# print(sys.path)

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0) # turn off animation,set delay in update drawing

rPaddle=Paddle((350,0))
lPaddle=Paddle((-350,0))
ball =Ball()



    
def esc():
    screen.exitonclick()

screen.listen()
screen.onkey(rPaddle.go_up,"Up")
screen.onkey(rPaddle.go_down,"Down")
screen.onkey(lPaddle.go_up,"w")
screen.onkey(lPaddle.go_down,"s")
screen.onkey(esc,"Escape")

gameOn=True

while gameOn:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()



screen.exitonclick()