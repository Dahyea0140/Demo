# Importing pandas and matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

netflix_subset = netflix_df[netflix_df["type"].str.strip() == "Movie"]
movies_1990 = netflix_subset[
    np.logical_and(
        netflix_subset["release_year"] >= 1990, netflix_subset["release_year"] < 2000
    )
]

plt.hist(movies_1990["duration"], bins=10, edgecolor="black")
plt.title("Frequent Movie Duration")
plt.xlabel("Duration in Mins")
plt.ylabel("Number of Movies")
plt.show()

duration = 100

action_movies_1990 = movies_1990[movies_1990["genre"] == "Action"]

short_movie_count = 0

for lab, row in action_movies_1990.iterrows():
    if row["duration"] < 90:
        short_movie_count += 1
    else:
        short_movie_count = short_movie_count

short_movie_count = 7
