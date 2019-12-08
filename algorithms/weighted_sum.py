#!/bin/python3
"""
Recommender algorithm

Weight sum of similarity vector
"""

import pandas as pd

WEIGHTS = [1, 1, 1, 1]

# rank, bgg_url, game_id, names, min_players, max_players, avg_time, min_time,
# max_time, year, avg_rating, geek_rating, num_votes, image_url, age, mechanic,
# owned, category, designer, weight


def recommend_similar(game_id, vectors, names, weights=None):
    """Recommend similar items to one that is provided as 1st argument

    weights is ordered list of weights given to each component in vector.
    v(geek_rating, category, mechanic, designer, weight)
    """
    if weights is None:
        weights = WEIGHTS

    series = []
    for key in vectors.keys():
        if key == game_id:
            series.append(None)
        else:
            series.append(weighted_sum(vectors[key], weights))

    return pd.DataFrame.from_dict({game_id: series}, orient='index',
                                  columns=names)


def weighted_sum(vector, weights):
    """Computes weighted sum of componentes of given network and its weights"""
    # v(category, mechanic, designer, weight)
    return sum(i*j for i, j in zip(vector, weights))
