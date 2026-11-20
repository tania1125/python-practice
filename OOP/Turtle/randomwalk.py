import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")

directions = [0, 90, 180, 270]

def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors


for _ in range(50):
    tim.pensize(5)
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.pencolor(random_colors)

