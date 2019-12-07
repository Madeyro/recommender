#!/bin/python3
"""
Recommender algorithm

1) Normalize Geek rating, which is average rating populated by 5.5 scores
for those games, which have small no ratings, or small amount of them.

2) Standardize authors, mechanics and category and compute % overlap
of key words separately.

3) More number of votes or more owned more relevant item.
"""

from random import randint
import pandas as pd

DATA_FILE = "board-game-data/bgg_db_1806.csv"

# rank, bgg_url, game_id, names, min_players, max_players, avg_time, min_time,
# max_time, year, avg_rating, geek_rating, num_votes, image_url, age, mechanic,
# owned, category, designer, weight


def get_random():
    """Return 10 random games"""
    # read from file to pandas
    data = pd.read_csv(DATA_FILE)

    # get random 10 games ids
    ids = set()
    while len(ids) < 10:
        ids.add(randint(1, len(data)))

    games = []
    for i in ids:
        games.append(data[data['rank'] == i])
    return games


if __name__ == "__main__":
    get_random()
