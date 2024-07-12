from turtle import Screen
import time

class GameScreen():

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor('black')
        self.screen.title(f"Pong Game")
        self.screen.tracer(0)
        self.screen.listen()

    def exit_game(self):
        self.screen.exitonclick()

    def update_screen(self):
        time.sleep(0.1)
        self.screen.update()

    def on_key_press(self, action, key):
        self.screen.onkey(action, key)