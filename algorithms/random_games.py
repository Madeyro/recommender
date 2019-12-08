#!/bin/python3
"""
Recommender algorithm

Get random 10 games
"""

from random import randint

# rank, bgg_url, game_id, names, min_players, max_players, avg_time, min_time,
# max_time, year, avg_rating, geek_rating, num_votes, image_url, age, mechanic,
# owned, category, designer, weight


def get_random(data):
    """Return 10 random games"""
    # get random 10 games ids
    ids = set()
    while len(ids) < 10:
        ids.add(randint(1, len(data)))

    games = []
    for i in ids:
        games.append(data[data['rank'] == i])
    return games
