#!/bin/python3
"""
Recommender algorithm

1) Normalize Geek rating, which is average rating populated by 5.5 scores
for those games, which have small no ratings, or small amount of them.

2) Standardize authors, mechanics and category and compute % overlap
of key words separately.
"""

from sys import argv
import pandas as pd
import utils

DATA_FILE = "board-game-data/bgg_db_1806.csv"

# rank, bgg_url, game_id, names, min_players, max_players, avg_time, min_time,
# max_time, year, avg_rating, geek_rating, num_votes, image_url, age, mechanic,
# owned, category, designer, weight


def main():
    """Recommend similiar items to one that is provided as 1st argument"""
    # read from file to pandas
    data = pd.read_csv(DATA_FILE)

    # normalize and standardize values
    data = utils.normalize(data, 'avg_rating')
    data = utils.standardize_text(data, 'category')
    data = utils.standardize_text(data, 'mechanic')
    data = utils.standardize_text(data, 'designer')

    # compute similarity to given game
    # each game has unique game_id

    # Text based: category, mechanic, designer
    # Number based:

    sorted_coeffs, coeffs = find_similar_text(data, int(argv[1]), 'category')
    ids = coeffs[sorted_coeffs[0]]
    for i in ids:
        print(data[data['game_id'] == i]['names'].values)


def find_similar_text(data, game_id, col_name):
    """Returns dictionary with similiar items.
    The key is similiar coeficient.
    """
    coeffs = {}
    for row in data.itertuples():
        if row.game_id == game_id:
            continue
        coeff = dice_coeff(data, row.game_id, game_id, col_name)
        if coeff in coeffs.keys():
            if isinstance(coeffs[coeff]) == list:
                coeffs[coeff].append(row.game_id)
            else:
                ids = [coeffs[coeff]]
                ids.append(row.game_id)
                coeffs[coeff] = ids
        else:
            coeffs[coeff] = row.game_id
    sorted_coeffs = sorted(coeffs.keys(), reverse=True)
    return sorted_coeffs, coeffs


def dice_coeff(data, x_game_id, y_game_id, col_name):
    """Computes dice similiarity coefficient"""
    x_game = data[data['game_id'] == x_game_id]
    y_game = data[data['game_id'] == y_game_id]
    return utils.dice_coeff(x_game[col_name], y_game[col_name])


if __name__ == '__main__':
    main()
