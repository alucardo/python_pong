from game_screen import GameScreen
from paddle import Paddle
from ball import Ball
import time

game_screen = GameScreen()
paddle_l = Paddle(game_screen, 'l')
paddle_r = Paddle(game_screen, 'r')
ball = Ball(game_screen)

game_start = True

while game_start:
    game_screen.update_screen()
    ball.move()
    time.sleep(0.1)

game_screen.exit_game()
