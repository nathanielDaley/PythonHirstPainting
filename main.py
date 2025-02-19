import random
import turtle
from turtle import Turtle, Screen

COLOR_LIST = [ (235, 240, 246), (247, 240, 243), (240, 246, 243), (133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209), (65, 66, 56), (103, 140, 129), (164, 200, 214), (130, 129, 122)]

turtle.colormode(255)

tim = Turtle()
screen = Screen()

tim.speed("fastest")
tim.penup()
tim.hideturtle()

dot_size = 50
x_starting_position = 0 - (dot_size * 9)
y_starting_position = 0 - (dot_size * 9)
y_offset = dot_size * 2

for x in range(10):
    tim.setposition(x_starting_position, y_starting_position + y_offset * x)
    for y in range(10):
        tim.color(random.choice(COLOR_LIST))
        tim.dot(dot_size)
        tim.forward(dot_size * 2)


screen.exitonclick()