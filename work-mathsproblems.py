# Math Problems
# Author: Ethan Lu
# November 14, 2025

# 3 math problems solved using python skills

def age_in_2049(age: int):
    return age+24

def olympic_judge_avg_score(scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive):
    return (scoreOne + scoreTwo + scoreThree + scoreFour  + scoreFive) / 5.0

def mcdolands_total(burger, fries):
    if burger == "yes":
        if fries == "yes":
            return (5.0 + 3.0) * 1.14
        else:
            return 5.0 * 1.14
    else:
        if fries == "yes":
            return 3.0 * 1.14
        else:
            return "you didn't even buy anything, why'd u come"

def main():
    age = int(input("How old are you now? "))
    print(f"In 2049 you will be {age_in_2049(age)} years old!")
    scoreOne = float(input("Judge 1: "))
    scoreTwo = float(input("Judge 2: "))
    scoreThree = float(input("Judge 3: "))
    scoreFour = float(input("Judge 4: "))
    scoreFive = float(input("Judge 5: "))
    print(f"Your Olympic Score is {olympic_judge_avg_score(scoreOne, scoreTwo, scoreThree, scoreFour, scoreFive)}")
    burger = input("Would you like a burger for $5 (Yes/No)").lower().strip("!.,? ")
    fries = input("Would you like fries for $3? (Yes/No)").lower().strip("!.,? ")
    print(f"Your total is ${mcdolands_total(burger, fries)}")

if __name__ == "__main__":
    main()
