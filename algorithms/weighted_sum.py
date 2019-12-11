#!/bin/python3
"""
Recommender algorithm

Weight sum of similarity vector
"""


WEIGHTS = [1, 1, 1, 1]

# rank, bgg_url, game_id, names, min_players, max_players, avg_time, min_time,
# max_time, year, avg_rating, geek_rating, num_votes, image_url, age, mechanic,
# owned, category, designer, weight


def recommend_similar(data, row, vectors, names, weights=None, count=20):
    """Recommend similar items to one that is provided as 1st argument

    weights is ordered list of weights given to each component in vector.
    v(geek_rating, category, mechanic, designer, weight)
    """
    if weights is None:
        weights = WEIGHTS

    coeffs = {}
    for key in vectors.keys():
        if key == row.game_id:
            continue
        coeffs[weighted_sum(vectors[key], weights)] = key

    return sort_dict_values(coeffs)


def weighted_sum(vector, weights):
    """Computes weighted sum of componentes of given network and its weights"""
    # v(category, mechanic, designer, weight)
    return sum(i*j for i, j in zip(vector, weights))


def sort_dict_values(coeffs):
    srted_keys = sorted(coeffs.keys(), reverse=True)

    cnt = 0
    srted = []
    for c, k in zip(coeffs.items(), srted_keys):
        srted.append(coeffs[k])
        cnt += 1
        if cnt == 20:
            break
    return srted
