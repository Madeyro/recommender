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
        similar_coeff = weighted_sum(vectors[key], weights)
        if similar_coeff in coeffs.keys():
            coeffs[similar_coeff].append(key)
        else:
            coeffs[similar_coeff] = [key]

    return sort_dict_values(data, coeffs)


def weighted_sum(vector, weights):
    """Computes weighted sum of componentes of given network and its weights"""
    # v(category, mechanic, designer, weight)
    return sum(i*j for i, j in zip(vector, weights))


def sort_dict_values(data, coeffs):
    srted_keys = sorted(coeffs.keys(), reverse=True)

    srted = []
    for c, k in zip(coeffs.items(), srted_keys):
        rank = []
        for item in coeffs[k]:
            rank.append(data.ix[data['game_id'] == item]['rank'].values[0])

        srted.append(rank)
        if len(srted) >= 20:
            break

    return srted
