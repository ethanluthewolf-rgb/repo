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
t.speed(1000000000000000000)

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

# Create a dictionary of leab colours
LEAF_COLOURS = {
    "spring": "#efc3e60"
}

def draw_complicated_tree(level: int, branch_length: float):
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
        t.left(55)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 4. Turn middle and draw a "smaller tree"
        t.right(55)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 5. Turn right and draw a "smaller tree"
        t.right(55)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 6. Return to the beginning
        t.left(55)
        t.backward(branch_length)
    else:
        # create a leaf
        t.color("green")
        t.stamp()
        t.color("brown")

def draw_rcomplicated_tree(level: int, branch_length: float):
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
        t.left(55)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        # 4. Turn middle and draw a "smaller tree"
        t.right(11)
        draw_complicated_tree(level - 1, branch_length * 0.8)
        t.right(11)
        draw_tree(level - 1, branch_length * 0.8)
        t.right(22)
        draw_rcomplicated_tree(level - 1, branch_length * 0.8)
        t.right(11)
        draw_complicated_tree(level - 1, branch_length * 0.8)

        # 5. Turn right and draw a "smaller tree"
        # 6. Return to the beginning
        t.backward(branch_length)
    else:
        # create a leaf
        t.color("green")
        t.stamp()
        t.color("brown")

def factorial(num: int) -> int:
    """Calculate the factoral of the given number recursively"""
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1;

def fibonacci(num: int) -> int:
    """Returns the nth fibonacci number calculated recursively"""
    # If the num is > 2
    if num > 2:
        return fibonacci(num-1) + fibonacci(num-2)
    else:
        return 1

print(fibonacci(5))
print(fibonacci(20))

wn.exitonclick()
