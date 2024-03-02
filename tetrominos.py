from turtle import Turtle
from constants import WIDTH, HEIGHT

SQUARE_LENGTH = 20


class SquareTetromino:

    def __init__(self):
        left_upper_square = self._create_square()
        left_upper_square.setposition(-SQUARE_LENGTH, (HEIGHT / 2) + SQUARE_LENGTH * 2)

        right_upper_square = self._create_square()
        right_upper_square.setposition(0, (HEIGHT / 2) + SQUARE_LENGTH * 2)

        left_lower_square = self._create_square()
        left_lower_square.setposition(-SQUARE_LENGTH, (HEIGHT / 2) + SQUARE_LENGTH)

        right_lower_square = self._create_square()
        right_lower_square.setposition(0, (HEIGHT / 2) + SQUARE_LENGTH)

        self.tetrominos = [left_lower_square, right_lower_square, left_upper_square, right_upper_square]

    def _create_square(self):
        square = Turtle("square")
        square.color("yellow")
        square.penup()
        return square



    # There should be some kind of abstract class for move, left, right, down and maybe rotate methods
    def move(self):
        for square in self.tetrominos:
            new_y = square.ycor() - SQUARE_LENGTH * 2
            if new_y < HEIGHT / -2:
                break
            square.sety(new_y)

    def left(self):
        for square in self.tetrominos:
            new_x = square.xcor() - SQUARE_LENGTH
            if new_x < WIDTH / -4:
                break
            square.setx(new_x)

    def right(self):
        for square in self.tetrominos:
            new_x = square.xcor() + SQUARE_LENGTH
            if new_x > WIDTH / 4:
                break
            square.setx(new_x)
