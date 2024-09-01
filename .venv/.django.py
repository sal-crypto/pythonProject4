import turtle as t
from turtle import Screen
import random
tom = t.Turtle()
tom.pensize(9)
tom.speed("fast")
#this colours has been taken from turtle documents:
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape (num_of_sides):
    angles = 360 / num_of_sides
    for i in range(num_of_sides):
#angles= 360/num_of_sides
        tom.forward(100)
        tom.right(angles)
for shape in  range( 3 , 11):
    tom.color(random.choice(colours))
    draw_shape(shape)


screen = Screen()
screen.exitonclick()

