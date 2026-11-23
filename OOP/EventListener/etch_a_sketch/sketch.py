""" CONTROLS OF SKETCH 
 W = FORWARDS
 S = BACKWARDS
 A = COUNTER-CLOCKWISE
 D = CLOCKWISE
 C = CLEAR DRAWING
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def w_move_forward():
    tim.forward(10)

def s_move_backwards():
    tim.forward(10)

def s_move_backwards():
    tim.backward(10)

def a_turn_left():
    heading = tim.heading() + 10
    tim.setheading(heading)

def d_turn_right():
    heading = tim.heading() - 10
    tim.setheading(heading)

def c_clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key= "w", fun=w_move_forward)
screen.onkey(key= "s", fun=s_move_backwards)
screen.onkey(key= "a", fun=a_turn_left)
screen.onkey(key= "d", fun=d_turn_right)
screen.onkey(key= "c", fun=c_clear_screen)

screen.exitonclick()