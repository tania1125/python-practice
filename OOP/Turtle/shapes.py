# Draw triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")

colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink",
    "brown", "black", "white", "gray", "cyan", "magenta", "lime",
    "maroon", "navy", "olive", "teal", "aqua", "silver", "gold",
    "indigo", "violet", "beige", "coral", "crimson", "khaki",
    "lavender", "salmon", "turquoise"
]

i=3
while i<= 10:
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)
    tim.pencolor(random.choice(colors))
    i +=1

screen = Screen()
screen.exitonclick()