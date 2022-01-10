from turtle import Turtle, Screen
import random

did_user_bet = False
sc = Screen()
sc.setup(width=500, height=400)
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_axis = [-70, -40, -10, 20, 50, 80]
turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis[index])
    turtles.append(new_turtle)

if user_bet:
    did_user_bet = True

while did_user_bet:
    for turtle in turtles:
        if turtle.xcor() == 230:
            did_user_bet = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner.")
            else:
                print(f"You lost. The {winning_turtle} was the winner.")

        distance = random.randint(0, 10)
        turtle.forward(distance)

sc.exitonclick()
