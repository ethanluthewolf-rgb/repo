# Choose your Own Adventure
# Ethan Lu
# October 6, 2025

#Ask the user what thhe weather is like
weather = input("What is the weather like? ")

if weather.lower().strip("!.,") == "rainy":
    print("You should bring an umbrella. ")
else:
    print("I see...")
