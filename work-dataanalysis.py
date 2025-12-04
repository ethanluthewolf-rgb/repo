# Data Analysis
# Author: Ethan Lu
# November 20, 2025

# Analyse the data provided in class

def main():
    # do your work in here
    # or create a new function and call it in here
    with open("data/NYC_Central_Park_weather_1869-2022.csv") as f:
        # remove first line from filestream
        _ = f.readline()

        counter = 0
        rainfall = 0.0
        min_temp = 0.0
        max_june_temp = 0.0

        for line in f:
            counter += 1
            info = line.split(",")
            if info[1] != "":
                # single_rainfall = float(info[1])
            if info[-2] != "":
                # single_min_temp = float(info[-2])

            # rainfall += single_rainfall
            # min_temp += single_min_temp


            # working on june max temps
            # idk how to fix
            date = info[0]
            if date[5:7] == "06":
                if info[-1] != "":
                    # single_max_june_temp = float(info[-1])

            # max_june_temp += single_max_june_temp

        rainfall /= counter
        min_temp /= counter
        max_june_temp /= counter
        min_temp = (min_temp - 32) * (5/9)
        print(counter)
        print(rainfall)
        print(min_temp)
        print(max_june_temp)



if __name__ == "__main__":
    main()
