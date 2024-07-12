from game_screen import GameScreen
from paddle import Paddle
import time

game_screen = GameScreen()
paddle_l = Paddle(game_screen, 'l')
paddle_r = Paddle(game_screen, 'r')

game_start = True

while game_start:
    game_screen.update_screen()
    time.sleep(0.1)

game_screen.exit_game()
