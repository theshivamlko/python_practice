from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.xMove=10
        self.yMove=10
    
    def move(self):
        newX=self.xcor()+ self.xMove
        newY=self.ycor()+ self.yMove
        self.goto(newX,newY)
        
    def bounce(self):
        self.xMove*=-1
        self.yMove*=-1  