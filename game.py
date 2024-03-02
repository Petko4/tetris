from turtle import Screen
from tetrominos import SquareTetromino
import time


class Game:

    def start(self):
        screen = Screen()
        # screen.tracer()
        screen.title("Tetris")
        screen.setup(width=600, height=600)
        screen.bgcolor("black")

        screen.tracer(0, 0)
        square_tetrominos = SquareTetromino()
        screen.update()

        screen.listen()
        screen.onkey(key="Left", fun=square_tetrominos.left)
        screen.onkey(key="Right", fun=square_tetrominos.right)

        while True:
            time.sleep(0.5)
            screen.tracer(0, 0)
            square_tetrominos.move()
            screen.update()

        screen.mainloop()

