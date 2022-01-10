import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

sc = Screen()
sc.setup(height=600, width=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_on = True
while game_on:
    sc.update()
    time.sleep(.09)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for part in snake.snake_body:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            game_on = False
            scoreboard.game_over()

sc.exitonclick()
