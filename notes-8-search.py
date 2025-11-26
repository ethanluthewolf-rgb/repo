# Intro to Search
# Author: Ubial
# 25 November

import csv

# Introduction to search algorithms
# Search for all songs by "Kendrick"
# Display all the YouTube and TikTok views
# Sort by either YouTube or TikTok views

def main():
    song_name_col = 0
    artist_col = 2
    yt_views_col = 11
    tiktok_views_col = 15
    artist1 = "Kendrick Lamar"
    artist2 = "Billie Eilish"

    # open the file
    with open("data/spotify2024.csv") as f:
        # get rid of the header row
        _ = f.readline()

        # create a reader object
        r = csv.reader(f)

        kendrick_songs = []
        billie_songs = []

        # go through reader line by line
        for info in r:
            # if the current artist is "Kendrick"
            if info[artist_col] == artist1:
                kendrick_songs.append(info)
            if info[artist_col] == artist2 and info[-1] != "1":
                billie_songs.append(info)


    print(f"Number of Kendrick Songs: {len(kendrick_songs)}")
    # print(billie_songs)
    print(f"Number of Billie Songs: {len(billie_songs)}")

    for song in kendrick_songs:
        current_trackname = song[song_name_col]
        current_ytviews = song[yt_views_col]
        current_tiktokviews = song[tiktok_views_col]

        # dispay information in a clear way
        # Track Name        YT Views        Tiktok Views
        print(f"{current_trackname}\t\t{current_ytviews}\t\t{current_tiktokviews}")

if __name__ == "__main__":
    main()
