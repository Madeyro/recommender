#!/bin/python3

import os.path
import pickle
import pandas as pd
import utils
import multiprocessing as mp
from vector_builder import build_vectors
from weighted_sum import recommend_similar as similar_weighted

DATA_FILE = "board-game-data/bgg_db_1806.csv"

# rank, bgg_url, game_id, names, min_players, max_players, avg_time, min_time,
# max_time, year, avg_rating, geek_rating, num_votes, image_url, age, mechanic,
# owned, category, designer, weight


def main():
    if os.path.isfile('normalized_data.csv'):
        data = pd.read_csv('normalized_data.csv')
    else:
        # read from file to pandas
        data = pd.read_csv(DATA_FILE)

        # remove rows with 0

        # normalize and standardize values
        data = utils.normalize(data, 'geek_rating')
        data = utils.normalize(data, 'avg_rating')
        data = utils.normalize(data, 'weight')
        data = utils.standardize_text(data, 'category')
        data = utils.standardize_text(data, 'mechanic')
        data = utils.standardize_text(data, 'designer')

        data.to_csv('normalized_data.csv')

    # with open('uw_matrix.pickle', 'rb') as handle:
    #     u = pickle.load(handle)

    # with open('w_matrix.pickle', 'rb') as handle:
    #     w = pickle.load(handle)

    # print(w[174430])

    compute_matrix(data, 0, len(data))


    # workers = 8
    # subset = int(len(data)/workers)
    # print("Dividing work into 8 parts")
    # parts = [[0, subset],
    #          [subset+1, 2*subset],
    #          [2*subset+1, 3*subset],
    #          [3*subset+1, 4*subset],
    #          [4*subset+1, 5*subset],
    #          [5*subset+1, 6*subset],
    #          [6*subset+1, 7*subset],
    #          [7*subset+1, len(data)]]

    # pool = mp.Pool(workers)
    # pool.starmap(compute_matrix,
    #              [(data, bound[0], bound[1]) for bound in parts])
    # pool.close()


def compute_matrix(data, start, end):
    w_matrix = {}
    uw_matrix = {}

    for i in range(start, end):
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
        ids = similar_weighted(data, row, vectors,
                               data.game_id.to_list())
        uw_matrix[row['rank']] = ids

        print("Computing weighted sum matrix")
        ids = similar_weighted(data, row, vectors,
                               data.names.to_list(),
                               weights=[0.5, 0.5, 0.2, 0.1])
        w_matrix[row['rank']] = ids

    if not os.path.isfile('uw_matrix.pickle'):
        with open('uw_matrix.pickle', 'wb') as handle:
            pickle.dump(w_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

    if not os.path.isfile('w_matrix.pickle'):
        with open('w_matrix.pickle', 'wb') as handle:
            pickle.dump(w_matrix, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return uw_matrix, w_matrix


if __name__ == '__main__':
    main()
