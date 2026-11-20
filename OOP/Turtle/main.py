from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

#draw square
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

# dotted lines
timmy_the_turtle.right(90)
timmy_the_turtle.teleport(150, -20)
timmy_the_turtle.right(90)

i=3
while i<12:
    timmy_the_turtle.teleport(-i * 10)
    timmy_the_turtle.forward(10)
    i +=2








screen = Screen()
screen.exitonclick()