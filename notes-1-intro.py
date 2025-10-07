# Notes - Introduction
# 16 September
# Ethan Lu

# Create an algorithm to solve a problem
# Problem: Create our own chatbot
# MeGPT

# 1. Greet the user with a predetermiined statement
greeting = "Hello! I am a chatbot!"

# 1a. Print the greeting
print(greeting)

# 2. Introduce the bot
print("My name is MeGPT.")
print("I'm not like the other guy.")
print("I am completely determnistic.")

# 3. Wow the user with some maths
print("I bet you don't know what 8*8 is.")
print("I can do it.")
print(f"8*8 is actually {8*8}.")

print("What is pi squared?")
print("I'm smart, I can do it too.")
print(f"It is {3.1415965359 ** 2}.")

# 4. Make the bot crash out a little bit.
print("The quick brown fox jums over the lazy dog." * 10)

# 5. Get the name of the user, store it, and use it
user_name = input("What's your name? ")
print(f"It's nice too meet you, {user_name}!")

# Chatbot

favourite_food = input("What's your favourite food? ")
print(f"{favourite_food}? That sounds delicious!")
favourite_hobby = input("What do you like to do in your free time? ")
print(f"{favourite_hobby} sounds pretty fun to do. Awesome!")
favourite_game = input("What's your favourite game? ")
print(f"You like Brawl Stars too? I love it as well! It's my favourite game! But I think {favourite_game} is an okay game too.")

# 8. See IF the user is someone specific.
# 8a. If they're someone specific, tell them a secret
if user_name == "Lebron James":
    print("You are my sunshine, my only sunshine.")
    print("Don't tell anyone I said this, my little sunshine. 🌻")

    favourite_book = input("What's your favourite book?")

    if favourite_book == "Harry Potter":
        print("I like Harry Potter, too!")
