# Big Data
# Author: Ubial
# 17 November

# Process files
# Ingest large data
# Make sense of data

def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)

    # Get information about the fave pizza place
    uncle_fatihs = 0
    club_ilia = 0
    pizza_hut = 0

    # Fave burrito place
    guadalupe = 0
    quesada = 0

    # Fave healthy food place
    subway = 0
    s_poke_bar = 0
    veggie_lunch = 0
    chopped_leaf = 0
    natures_garden = 0

    for line in file:
        # fave pizza is in column 5 (4th ind)
        # a line is a string
        # convert the string to a list
        # split the line wherever a , is
        info = line.split(",")
        fave_pizza = info[4]
        fave_burrito = info[5]
        fave_healthy = info[6]

        if fave_pizza == "Uncle Fatih's":
            uncle_fatihs += 1
        elif fave_pizza == "Club Ilia":
            club_ilia += 1
        elif fave_pizza == "Pizza Hut":
            pizza_hut += 1

        if fave_burrito == "Guadalupe (MBC)":
            guadalupe += 1
        elif fave_burrito == "Quesada (Cornerstone)":
            quesada += 1

        if fave_healthy == "Subway":
            subway += 1
        elif fave_healthy == "Steve's Poke Bar":
            s_poke_bar += 1
        elif fave_healthy == "Veggie Lunch":
            veggie_lunch += 1
        elif fave_healthy == "Chopped Leaf":
            chopped_leaf += 1
        elif fave_healthy == "Nature's garden":
            natures_garden += 1


    # Display Results
    print(f"Uncle Fatih's Votes: {uncle_fatihs}")
    print(f"Club Ilia votes: {club_ilia}")
    print(f"Pizza Hut votes: {pizza_hut}")

    print(f"Subway's Votes: {subway}")
    print(f"Steve's Poke Bar's Votes: {s_poke_bar}")
    print(f"Veggie Lunch's Votes: {veggie_lunch}")
    print(f"Chopped Leaf's Votes: {chopped_leaf}")
    print(f"Nature's garden's Votes: {natures_garden}")

    # Display the most popular burrito place
    if guadalupe > quesada:
        print("Guadalupe is the most popular burrito place.")
    elif guadalupe == quesada:
        print("It's a tie! Guadalupe and Quesada both win!")
    else:
        print("Quesada is the most popular burrito place.")

    file.close()


if __name__ == "__main__":
    main()
