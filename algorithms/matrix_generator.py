#!/bin/python3

import os.path
import pickle
import pandas as pd
import utils
from vector_builder import build_vectors
from weighted_sum import recommend_similar as similar_weighted

DATA_FILE = "board-game-data/bgg_db_1806.csv"

# rank, bgg_url, game_id, names, min_players, max_players, avg_time, min_time,
# max_time, year, avg_rating, geek_rating, num_votes, image_url, age, mechanic,
# owned, category, designer, weight

if os.path.isfile('normalized_data.csv'):
    data = pd.read_csv('normalized_data.csv')
else:
    # read from file to pandas
    data = pd.read_csv(DATA_FILE)

    # normalize and standardize values
    data = utils.normalize(data, 'geek_rating')
    data = utils.normalize(data, 'avg_rating')
    data = utils.normalize(data, 'weight')
    data = utils.standardize_text(data, 'category')
    data = utils.standardize_text(data, 'mechanic')
    data = utils.standardize_text(data, 'designer')

    data.to_csv('normalized_data.csv')

w_matrix = {}
uw_matrix = {}

for i in range(len(data)):
    row = data.loc[i]
    print(row.names)
    print("Computing similarity vectors")
    if os.path.isfile(f'vectors/{row.game_id}.pickle'):
        with open(f'vectors/{row.game_id}.pickle', 'rb') as handle:
            vectors = pickle.load(handle)
    else:
        vectors = build_vectors(data, row.game_id, 'jaccard_coeff')
        with open(f'vectors/{row.game_id}.pickle', 'wb') as handle:
            pickle.dump(vectors, handle, protocol=pickle.HIGHEST_PROTOCOL)

    print("Computing unweighted sum matrix")
    uw_matrix[row.game_id] = similar_weighted(row.game_id, vectors,
                                              data.names.to_list())

    print("Computing weighted sum matrix")
    w_matrix[row.game_id] = similar_weighted(row.game_id, vectors,
                                             data.names.to_list(),
                                             weights=[0.5, 0.5, 0.2, 0.1])

    if i == 5:
        break

if os.path.isfile('uw_matrix.pickle'):
    with open('uw_matrix.pickle', 'rb') as handle:
        uw_matrix = pickle.load(handle)
else:
    with open('uw_matrix.pickle', 'wb') as handle:
        pickle.dump(w_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

if os.path.isfile('w_matrix.pickle'):
    with open('w_matrix.pickle', 'rb') as handle:
        w_matrix = pickle.load(handle)
else:
    with open('w_matrix.pickle', 'wb') as handle:
        pickle.dump(w_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

for k in w_matrix.keys():
    print(w_matrix[k].iloc[0].sort_values())
