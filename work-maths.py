# Maths Stuff with Python
# Author: Ubial
# 12 November 2025

import math

# Do math things with Python
# Machines are good at crunching numbers - faster
# and more accurately than most humans!
# Create a small program that calculates something useful
# to you (making you smile is useful). It should take
# user input, at use at least one of the number
# operators we saw in class: + / * -. You may modify one
# of your previous exercises to include calculations,
# if you wish.

'''
def pythagorean_theorem(a: int, b: int) -> int:
    return math.sqrt((a ** 2) + (b ** 2))

def main():
    print("What are the two sides of the triangle.")
    print("The two shorter ones.")

    a = int(input("a: "))
    b = int(input("b: "))

    print(f"The hypotenuse is {pythagorean_theorem(a, b)}!")

if __name__ == "__main__":
    main()

'''

def movie_rater():
    movie = input("What's the movie you're rating? ")
    print(f"This function will calculate a rating for {movie}.")
    print("Give a rating from 1-5.")
    intro = int(input("How was the intro? "))
    characters = int(input("How were the characters? "))
    plot = int(input("How was the plot? "))
    climax = int(input("How was the climax? "))
    end = int(input("How was the ending? "))
    rating = (intro + characters + plot + climax + end) / 5.0
    print(f"Your final rating is... {rating}!")

movie_rater()
