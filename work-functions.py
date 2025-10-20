# Functions
# Author: Ethan Lu
# 10 October 2025

# In your `work-functions.py` file, create a function that calculates the average of three numbers. Here are the requirements in detail:
#
# * call it `average`
# * it should accept three parameters: `num_one`, `num_two`, and `num_three`
# * it should calculate the average value of the three numbers:
# 	* recall that to calculate the average, you add the values then divide by the number of values you have
# * return the result
#
#  *Optional*: write another version that accepts a list and returns the average of all things inside the list

def average(num_one: int, num_two: int, num_three: int):
    return (num_one + num_two + num_three) / 3

print(average(101, 98, 92))
