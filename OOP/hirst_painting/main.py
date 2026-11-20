import turtle as t
import random

color_list = [(236, 224, 81), (197, 7, 72), (201, 75, 15), (113, 178, 214), (196, 164, 13), (231, 54, 132), (217, 162, 102), (28, 105, 168)]

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()
j = 1
while j<= 10:
    for i in range(10):
        tim.color(random.choice(color_list))
        tim.circle(20)
        tim.teleport(50 * (i+1))
    print(tim.position())
    tim.teleport(450, 50*j)
    j += 1
    

screen.exitonclick()