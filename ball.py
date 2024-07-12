from turtle import Turtle

class Ball(Turtle):

    def __init__(self, game_screen):
        super().__init__()
        self.game_screen = game_screen
        self.penup()
        self.color('blue')
        self.shape('circle')

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)