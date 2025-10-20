# Drawing and loops
# Author: Ethan u
# 14 October, 2025

import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightblue")

# TMNT - turtles
# create a turtle named Mike
mike = turtle.Turtle()
mike.turtlesize(5)  # set size
mike.shape("turtle") # shape
mike.color("orange") # colour

# move mike around
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.forward(50)
mike.left(30)
mike.penup()
mike.left(103)
mike.forward(50)
mike.pendown()
mike.right(120)
mike.forward(40)
mike.left(33)
mike.forward(40)
mike.left(77)
mike.penup()
mike.forward(60)
mike.pendown()
mike.forward(5)
mike.left(90)
mike.forward(5)
mike.left(90)
mike.forward(5)
mike.left(90)
mike.forward(5)
mike.left(177)
mike.penup()
mike.forward(60)
mike.pendown()
mike.forward(5)
mike.right(90)
mike.forward(5)
mike.right(90)
mike.forward(5)
mike.right(90)
mike.forward(5)
mike.right(90)
mike.penup()
mike.forward(200)

mike.pendown()
mike.circle(100)
mike.penup()
mike.goto(-200, 200)
mike.pendown()
mike.circle(50)
mike.penup()
mike.goto(-200, 250)
mike.pendown()
mike.circle(25)

for counter in range(100):
    counter = counter * 50
    # Cookie Making
    # Set the colour of our choco chip cookie
    mike.color("brown")
    # Draw a circle to represent our cookie
    mike.shapesize(1)
    mike.pu()
    mike.setheading(0)   # mike points east
    mike.goto(-5 + counter, -30 + counter)
    mike.pd()
    mike.circle(30)
    # Put a chocolate chip at the top-right
    mike.pu()
    mike.goto(10 + counter, 10 + counter)
    mike.stamp()
    # Put a chocolate chip at the bottom-right
    mike.goto(10 + counter, -10 + counter)
    mike.stamp()
    # Put a choco chip at the bottom-left
    mike.goto(-10 + counter, -10 + counter)
    mike.stamp()
    # Choco chip at the top-left
    mike.goto(-10 + counter, 10 + counter)
    mike.stamp()
    # Chocolate chip in the middle
    mike.goto(0 + counter, 0 + counter)
    mike.stamp()

window.exitonclick()
