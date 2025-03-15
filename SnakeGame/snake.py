from multiprocessing.reduction import send_handle
from turtle import Turtle
MOVE_RANGE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_shapes = []
        self.create_shapes(3)
        self.head = self.snake_shapes[0]

    def create_shapes(self, num_of_shapes):
        for s in range(num_of_shapes):
            shape = Turtle("square")
            shape.color("white")
            shape.penup()
            x_pos = shape.xcor()
            y_pos = shape.ycor()
            shape.goto(x_pos, y_pos)
            self.snake_shapes.append(shape)
            x_pos -= 20

    def add_tail(self):
        x_pos = self.snake_shapes[-1].xcor()
        y_pos = self.snake_shapes[-1].ycor()
        new_tail = Turtle("square")
        new_tail.penup()
        new_tail.goto(x_pos, y_pos)
        self.snake_shapes.append(new_tail)
        new_tail.color("white")

    def check_tail_collision(self):
        for shape in self.snake_shapes[3:]:
            if self.head.distance(shape) < 20:
                return True

    def move(self):
        for square in range(len(self.snake_shapes) - 1, 0, -1):
            new_x_pos = self.snake_shapes[square - 1].xcor()
            new_y_pos = self.snake_shapes[square - 1].ycor()
            self.snake_shapes[square].goto(new_x_pos, new_y_pos)
        self.snake_shapes[0].forward(MOVE_RANGE)

    def up(self):
        direction = self.head.heading()
        if direction == RIGHT:
            self.head.setheading(UP)
        elif direction == LEFT:
            self.head.setheading(UP)


    def down(self):
        direction = self.snake_shapes[0].heading()
        if direction == RIGHT:
            self.snake_shapes[0].setheading(DOWN)
        elif direction == LEFT:
            self.snake_shapes[0].setheading(DOWN)

    def left(self):
        direction = self.snake_shapes[0].heading()
        if direction == UP:
            self.snake_shapes[0].setheading(LEFT)
        elif direction == DOWN:
            self.snake_shapes[0].setheading(LEFT)

    def right(self):
        direction = self.snake_shapes[0].heading()
        if direction == DOWN:
            self.snake_shapes[0].setheading(RIGHT)
        elif direction == UP:
            self.snake_shapes[0].setheading(RIGHT)
