from turtle import Turtle

class Ball(Turtle):

    def __init__(self, game_screen):
        super().__init__()
        self.game_screen = game_screen
        self.penup()
        self.color('blue')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        if self.wall_collision():
            self.bounce()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_collision(self):
        return self.ycor() > 280 or self.ycor() < -280

    def bounce(self):
        self.y_move *= -1