#!/bin/python3
"""
Recommender algorithm helper

1) Normalize Geek rating, which is average rating populated by 5.5 scores
for those games, which have small no ratings, or small amount of them.

2) Standardize authors, mechanics and category and compute % overlap
of key words separately.

3) Create vector v with attributes:
(geek_rating, category, mechanic, designer, weight)
"""

import utils

# rank, bgg_url, game_id, names, min_players, max_players, avg_time, min_time,
# max_time, year, avg_rating, geek_rating, num_votes, image_url, age, mechanic,
# owned, category, designer, weight


def build_vectors(data, game_id, simm_coeff):
    """Build similiarity vector to provided game for each board game

    v(geek_rating, category, mechanic, designer, weight)
    """
    # Text based: category, mechanic, designer
    # Number based: weight
    # Create vector v with attributes above:
    # v(category, mechanic, designer, weight)

    # compute similarity to given game
    # each game has unique game_id
    return compute_similiarity(data, game_id, simm_coeff)


def compute_similiarity(data, game_id, simm_coeff):
    text_factors = ['category', 'mechanic', 'designer']
    vectors = {}

    for i in range(len(data)):
        row = data.loc[i]
        vectors[row.game_id] = []
        if row.game_id == game_id:
            vectors[row.game_id] = None
            continue
        for factor in text_factors:
            coeff = get_coeff(data, row.game_id, game_id, factor, simm_coeff)
            vectors[row.game_id].append(coeff)
        vectors[row.game_id].append(row.weight)
    return vectors


def find_similar_text(data, game_id, col_name):
    """Returns dictionary with similiar items.
    The key is similiar coeficient.
    """
    coeffs = {}
    for row in data.itertuples():
        if row.game_id == game_id:
            continue
        coeff = get_coeff(data, row.game_id, game_id, col_name)
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


def get_coeff(data, x_game_id, y_game_id, col_name, simm_coeff):
    """Computes dice similiarity coefficient on sets"""
    x_game = data[data['game_id'] == x_game_id]
    y_game = data[data['game_id'] == y_game_id]
    return getattr(utils, simm_coeff)(x_game[col_name], y_game[col_name])
