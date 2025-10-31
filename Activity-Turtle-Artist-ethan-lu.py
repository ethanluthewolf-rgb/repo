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
t.speed(1000000000000)

# Starry night with variable star sizes

# Star function
def drawStar(size: int, color):
    t.pendown()
    if color.lower().strip("!.,? ") == "red" or color.lower().strip("!.,? ") == "orange" or color.lower().strip("!.,? ") or "yellow" or color.lower().strip("!.,? ") == "white" or color.lower().strip("!.,? ") == "blue" or color.lower().strip("!.,? ") == "purple":
        t.fillcolor(color)
        t.begin_fill()
        t.setheading(90)
        t.


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
t.left(160)
t.forward(75)
t.right(85)
t.forward(10)
t.left(85)
t.forward(30)
t.left(23)
t.forward(13)
t.right(20)
t.forward(150)
t.right(163)
t.forward(30)
t.right(15)
t.forward(130)
t.left(45)
t.forward(35)
t.right(40)
t.forward(140)
t.left(15)
t.forward(130)
t.left(15)
t.forward(20)
t.left(160)
t.forward(40)
t.right(35)
t.forward(45)
t.left(180)
t.forward(20)
t.left(70)
t.forward(120)
t.right(35)
t.forward(80)
t.left(35)
t.forward(60)
t.right(30)
t.forward(80)
t.right(108)
t.forward(250)
t.end_fill()
t.penup()

# Stars
t.goto(-390, 340)
t.pendown()
drawStar(20, "yellow")




wn.exitonclick()
