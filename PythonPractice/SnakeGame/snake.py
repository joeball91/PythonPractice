from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        body_part = Turtle("square")
        body_part.color("white")
        body_part.penup()
        body_part.goto(position)
        self.snake_body.append(body_part)

    def extend (self):
        self.add_part(self.snake_body[-1].position())

    def move(self):
        for piece in range(len(self.snake_body) - 1, 0, -1):
            next_x = self.snake_body[piece - 1].xcor()
            next_y = self.snake_body[piece - 1].ycor()
            self.snake_body[piece].goto(next_x, next_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def reset(self):
        for part in self.snake_body:
            part.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)
