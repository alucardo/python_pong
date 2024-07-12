from turtle import Turtle

class Ball(Turtle):

    def __init__(self, game_screen, paddle_r, paddle_l):
        super().__init__()
        self.game_screen = game_screen
        self.paddle_r = paddle_r
        self.paddle_l = paddle_l

        self.penup()
        self.color('blue')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.check_wall_collision()
        self.check_paddle_collision()
        self.check_right_point()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.game_screen.update_screen()


    def check_right_point(self):
        if self.xcor() > 350:
            self.reset()

    def check_right_point(self):
        if self.xcor() < -350:
            self.reset()
    def check_wall_collision(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def check_paddle_collision(self):
        if self.paddle_collision_r() or self.paddle_collision_l():
            self.bounce_x()
    def paddle_collision_r(self):
        return self.distance(self.paddle_r) < 50 and self.xcor() > 320

    def paddle_collision_l(self):
        return self.distance(self.paddle_l) < 50 and self.xcor() < -320

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.bounce_x()
        self.goto(0, 0)