from turtle import Turtle

A_PADDLE = 350
UP = 90
DOWN = 270
STEP = 10

class Paddle(Turtle):
    def __init__(self, game_screen, version):
        super().__init__()
        self.game_screen = game_screen
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        if version == 'r':
            self.goto(350, 0)
            self.game_screen.on_key_press(self.up, "Up")
            self.game_screen.on_key_press(self.down, "Down")
        else:
            self.goto(-350, 0)
            self.game_screen.on_key_press(self.up, "w")
            self.game_screen.on_key_press(self.down, "s")

    def up(self):
        new_y = self.ycor() + STEP
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - STEP
        self.goto(self.xcor(), new_y)