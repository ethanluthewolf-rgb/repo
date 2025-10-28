import time
import os
import sys

# Choose your Own Adventure
# Ethan Lu
# September 24, 2025

# Choose your own adventure solely focusing on
# using variables and branching/conditionals

def restart_program():
    """Restarts the current program."""
    python = sys.executable
    os.execv(python, ['python'] + sys.argv)

def game():
    # Introduction
    time.sleep(0.5)
    print("You wake up in a sterile white room with no windows.")
    time.sleep(0.5)
    print("A headache attacks you while a synthetic voice crackles to life.")
    time.sleep(0.5)
    print("\"Subject 12. Consciousness upload successful. Welcome to Fracture Point.\"")
    time.sleep(0.5)
    print("You see two doors infront of you: on the left, a door labeled \"MEMORY CORE\", and on the right, \"EXTRACTION BAY\".")
    time.sleep(0.5)
    print("\"Time is breaking. Choose wisely.\"")

    # Problem

    choiceOne = input("Type 1 to open the left door marked \"MEMORY CORE\".\nType 2 to open the right door marked \"EXTRACTION BAY\".")
    while choiceOne != "1" and choiceOne != "2":
        print("Please type 1 or 2.")
        choiceOne = input("Type 1 to open the left door marked \"MEMORY CORE\".\nType 2 to open the right door marked \"EXTRACTION BAY\".")

    # Rising Action

    if choiceOne == "1":
        print("You enter a room filled with floating orbs. Each one shows glimpses of your possible paths—a soldier, a scientist, a fugitive. One orb pulses stronger than the rest.")
        choiceOneBranch = input("Do you: \n1. Touch the pulsing orb \n2. Break the orb \n3. Ignore all orbs and leave")
        while choiceOneBranch != "1" and choiceOneBranch != "2" and choiceOneBranch != "3":
            print(f"Sorry, I don't understand {choiceOneBranch}.")
            print("Please type 1, 2, or 3.")
            choiceOneBranch = input("Do you: \n1. Touch the pulsing orb \n2. Break the orb \n3. Ignore all orbs and leave")
        if choiceOneBranch == "1":
            # Climax
            print("You touch the orb and you suddenly get teleported to a lab. You become a well-respected scientist there and become the head scientist of the lab experimenting with multiple timelines. ")
            # Resolution
            print("You have unlocked the ending: \"The Renegade Scientist\"")
        elif choiceOneBranch == "2":
            # Climax
            print("You erased your past identity and you walk onto a path even you don't know where it leads. ")
            # Resolution
            print("You have unlocked the ending: \"My Own Path\"")
        elif choiceOneBranch == "3":
            # Climax
            print("You ignored all the orbs and left, remaining a black state ")
            # Resolution
            print("You have unlocked the ending: \"My Own Path\"")

    elif choiceOne == "2":
        print("You're greeted by a woman in a lab coat who calls you \"Commander Vale\"—but you're not sure if she’s lying.")
        choiceTwoBranch = input("Do you: \n1. Pretend to be Commander Vale \n2. Admit you don't remember \n3. Attack her first")
        while choiceTwoBranch != "1" and choiceTwoBranch != "2" and choiceTwoBranch != "3":
            print(f"Sorry, I don't understand {choiceTwoBranch}.")
            print("Please type 1, 2, or 3.")
            choiceTwoBranch = input("Do you: \n1. Pretend to be Commander Vale \n2. Admit you don't remember \n3. Attack her first")
        if choiceTwoBranch == "1":
            # Climax
            print("You gain her trust, and you unlock base access, leading to you becoming a scientist working there.")
            # Resolution
            print("You have unlocked the ending: \"The Scientist\"")
        elif choiceTwoBranch == "2":
            # Climax
            print("She quickly runs and activates a failsafe, and you are arrested in seconds, and then placed into a jail for who knows how long.")
            # Resolution
            print("You have unlocked the ending: \"Prisoner of Time\"")
        elif choiceTwoBranch == "3":
            # Climax
            print("You attack her and become violent, becoming an unstable person who walks a dangerous path where you are hunted.")
            # Resolution
            print("You have unlocked the ending: \"Fractured Mind\"")

while True:
    start = input("Start Game? Type YES/NO ").lower()
    if start == "yes":
        game()
        restart = input("Enter anything to restart. ")
        restart_program()
    elif start == "no":
        restart = input("Game not started. Press r to restart.")
        if restart == "r":
            print("Restarting program...")
            restart_program()
    else:
        print("Invalid input. Please enter \"YES\" or \"NO\".")
        invalid = input("Press r to restart.")
        if invalid == "r":
            print("Restarting program...")
            restart_program()
