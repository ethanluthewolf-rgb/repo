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
t.color("blue")

# Recursive function that splits a cubes into 8 pieces
def drawCube(level: int, length: int):
    if level > 1:
        drawCube(level - 1, length / 2)
    else:
        t.pendown()
        t.forward(length)
        t.left(65)
        t.forward(length)
        t.left(115)
        t.forward(length)
        t.left(65)
        t.forward(length)
        t.left(50)
        t.forward(length)
        t.left(65)
        t.forward(length)
        t.left(65)
        t.forward(length)
        t.left(50)
        t.forward(length)
        t.right(230)
        t.forward(length)
        t.left(50)
        t.forward(length)
        t.right(115)
        t.forward(length)
        t.right(115)
        t.forward(length)
        t.right(65)
        t.forward(length)
        t.right(180)
        t.forward(length)
        t.right(65)
        t.forward(length)
        t.left(130)


drawCube(3, 100)

wn.exitonclick()
