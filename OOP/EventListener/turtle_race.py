from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
positions = [-100, -50, 0, 50, 100, 150]
colors = ["red", "orange", "yellow", "green", "blue", "purple" ]
turtle_participants = []

screen.setup(width=500, height=500)
screen.colormode(255)

for i in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, positions[i])
    turtle_participants.append(new_turtle)

user_choice = screen.textinput("TURTLE RACE", "Who will win the race? Enter a colour").lower()

if user_choice:
    is_race_on = True
    

while is_race_on:
    for turtle in turtle_participants:
        if turtle.xcor() > 230:
            if user_choice == turtle.pencolor():
                print("You won!!! The turtle you bet on has won")
            else:
                print(f"You Lost!!! The {user_choice} turtle you bet on lost,  {turtle.pencolor()} turtle won the match " )    
            is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()