from game_screen import GameScreen
from paddle import Paddle
from ball import Ball


game_screen = GameScreen()
paddle_l = Paddle(game_screen, 'l')
paddle_r = Paddle(game_screen, 'r')
ball = Ball(game_screen, paddle_r, paddle_l)

game_start = True

while game_start:
    ball.move()

game_screen.exit_game()
