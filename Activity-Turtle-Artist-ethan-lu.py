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
t.color("black")
t.width(5)
t.fillcolor("darkblue")

# Starry night with variable star sizes

# Frame
t.goto(-460, -370)
t.begin_fill()
t.pendown()
t.forward(740)
t.right(90)
t.forward(920)
t.right(90)
t.forward(740)
t.right(90)
t.forward(920)
t.end_fill()

# Mountain
t.penup()
t.fillcolor("black")
t.goto(-294, -370)
t.right(60)
t.pendown()
t.begin_fill()
t.forward(145)
t.right(40)
t.forward(70)
t.left(15)
t.forward(100)
t.right(15)
t.forward(90)
t.left(22)
t.forward(45)
t.right(12)
t.forward(45)
t.right(167)
t.forward(60)
t.left(150)

# Star function
def drawStar(size: int, color):
    if color.lower().strip("!.,? ") == "red":
        t.color("red")
    elif color.lower().strip("!.,? ") == "orange":
        t.color("orange")
    elif color.lower().strip("!.,? ") == "yellow":
        t.color("yellow")
    elif color.lower().strip("!.,? ") == "white":
        t.color("white")
    elif color.lower().strip("!.,? ") == "blue":
        t.color("blue")
    elif color.lower().strip("!.,? ") == "purple":
        t.color("purple")
    else:
        print(f"{color} is not a valid color. Please try red, orange, yellow, white, blue, or purple.")


wn.exitonclick()
