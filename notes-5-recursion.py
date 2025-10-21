# Recursion
# Author: Ethan Lu
# Oct 20, 2025

# Create a function that draws trees recursively

import turtle

# Set up the environment
wn = turtle.Screen()
t = turtle.Turtle()
t.left(90)               # point the turtle upp
t.penup()                # move the turtle a little lower
t.goto(0, -200)
t.color("brown")
t.width(10)
t.shape("arrow")         # leaf shape

def draw_tree(level: int, branch_length: float):
    """Draw a tree recursively at a given level
    level - the levels of branches
    branch_length - length of branch in pixels
    """
    t.pendown()

    # If the level is greater than zero
    if level > 0:
        # 1. Move forward branch_length
        t.forward(branch_length)
        # 2. Turn left and draw a "smaller tree"
        t.left(45)
        draw_tree(level - 1, branch_length * 0.8)
        # 3. Turn right and draw a "smaller tree"
        t.right(90)
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Return to the beginning
        t.left(45)
        t.backward(branch_length)
    else:
        # create a leaf
        t.color("green")
        t.stamp()
        t.color("brown")

draw_tree(6, 200)

wn.exitonclick()
