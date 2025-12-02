# Advent Of Code
# Author: Ethan Lu
# December 1, 2025

def part_one():
    # read every line in the instructions
    with open("data/aoc-2025-day1.txt") as f:
        temp = 0
        count = 50
        password = 0
        for line in f:
            temp = int(line[1:len(line)+1]) % 100
            if line[0:1] == "L":
                if (count - temp) < 0:
                    count = 100 - temp
                else:
                    count -= temp
            elif line[0:1] == "R":
                if (count + temp) > 100:
                    count = 0 + temp
                else:
                    count += temp
            else:
                print("invalid")
            if count == 0 or count == 100:
                password += 1
    # instruction exampe "R10" -> right 10
    # if we go RIGHT -> add
    # if we go left -> subtract
    # if we land on zero keep track of it
    # print how many times we landed on zero

    print(password)

if __name__== "__main__":
    part_one()
