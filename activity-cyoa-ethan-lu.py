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
    clarity = 0; # represents mental stabiity and self awareness
    # trust tracks relationships and cooperation
    trustEcho = 0;
    trustMarris = 0;
    trustMirror = 0;
    trustRyne = 0;
    fracture = 0; # represents instability, paradox risk, memory corruption
    # Introduction
    time.sleep(1)
    print("You wake up in a sterile white room with no windows.")
    time.sleep(3)
    print("A headache attacks you while a synthetic voice crackles to life.")
    time.sleep(3)
    print("\"Subject 12. Consciousness upload successful. Welcome to Fracture Point.\"")
    time.sleep(3)
    print("You see two doors infront of you: on the left, a door labeled \"MEMORY CORE\", and on the right, \"EXTRACTION BAY\".")
    time.sleep(3)
    print("\"Time is breaking. Choose wisely.\"")

    # Problem

    choiceOne = input(f"Type 1 to open the left door marked \"MEMORY CORE\".\nType 2 to open the right door marked \"EXTRACTION BAY\".")
    while choiceOne != "1" and choiceOne != "2":
        print("Please type 1 or 2.")
        choiceOne = input(f"Type 1 to open the left door marked \"MEMORY CORE\".\nType 2 to open the right door marked \"EXTRACTION BAY\".")

    # Rising Action

    if choiceOne == "1":
        print(f"You enter a room filled with floating orbs. Each one shows glimpses of your possible paths—a soldier, a scientist, a fugitive. One orb pulses stronger than the rest.")
        choiceOneBranch = input(f"Do you: \n1. Touch the pulsing orb \n2. Break the orb \n3. Ignore all orbs and leave")
        if choiceOneBranch == "1":
            print(f"You touch the orb and you suddenly get teleported to a lab. You become a well-respected scientist there and become the head scientist of the lab experimenting with multiple timelines. ")
            print(f"You have unlocked the ending: \"The Renegade Scientist\"")
            restart = input(f"Press r to restart game.")
            if restart == "r":
                print("Restarting program...")
                restart_program()
    elif choiceOne == "2":
        print("You're greeted by a woman in a lab coat who calls you \"Commander Vale\"—but you're not sure if she’s lying.")


while True:
    start = input(f"Start Game? Type YES/NO ").lower()
    if start == "yes":
        game()
    elif start == "no":
        restart = input(f"Game not started. Press r to restart.")
        if restart == "r":
            print("Restarting program...")
            restart_program()
    else:
        print("Invalid input. Please enter \"YES\" or \"NO\".")
        invalid = input(f"Press r to restart.")
        if invalid == "r":
            print("Restarting program...")
            restart_program()



# Climax

# Resolution
