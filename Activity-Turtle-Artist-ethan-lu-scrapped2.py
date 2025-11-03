# Turtle Artist
# Author: Ethan Lu
# 28 October

import turtle

# A one-of-a-kind drawing

wn = turtle.Screen()
t = turtle.Turtle()

# Your code here
t.penup()
t.width(5)
t.left(90)
t.color("yellow")

# Recursive function that splits a square into 4 pieces
def drawSquare(level: int, length: int):
    t.pendown()
    if level > 0:
        drawSquare(level - 1, length / 4)
        t.forward(length/4)
        drawSquare(level - 1, length / 4)
        t.right(90)
        t.forward(length/4)
        t.left(90)
        drawSquare(level - 1, length / 4)
        t.left(180)
        t.forward(length/4)
        t.right(180)
        drawSquare(level - 1, length / 4)
        t.left(90)
        t.forward(length/4)
        t.right(90)
    else:
        t.forward(length)
        t.right(90)
        t.forward(length)
        t.right(90)
        t.forward(length)
        t.right(90)
        t.forward(length)
        t.right(90)

t.fillcolor("yellow")
t.pendown()
t.begin_fill()
t.right(15)
t.forward(40)
t.right(150)
t.forward(40)
t.left(75)
t.forward(40)
t.right(150)
t.forward(40)
t.left(75)
t.forward(40)
t.right(155)
t.forward(40)
t.left(105)
t.forward(40)
t.right(155)
t.forward(44)
t.left(75)
t.forward(40)
t.right(155)
t.forward(40)
t.end_fill()

wn.exitonclick()
