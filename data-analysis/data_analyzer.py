#!/bin/python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# rank, bgg_url, game_id, names, min_players, max_players, avg_time, min_time,
# max_time, year, avg_rating, geek_rating, num_votes, image_url, age, mechanic,
# owned, category, designer, weight

DATA_FILE = "board-game-data/bgg_db_1806.csv"
DIR = "data-analysis/"
IMG_DIR = DIR + "img/"
STATS_DIR = DIR + "stats/"
NUM_STATS = STATS_DIR + "num_analysis.csv"
CAT_STATS = STATS_DIR + "cat_analysis.csv"
CAT_COUNT = STATS_DIR + "cat_count.csv"


def main():
    # read from file to pandas
    data = pd.read_csv(DATA_FILE)

    # save basic statistics
    cols = ['avg_rating', 'geek_rating', 'num_votes', 'owned', 'min_players',
            'max_players', 'avg_time', 'min_time', 'max_time']

    data[cols].describe() \
              .transpose() \
              .to_csv(NUM_STATS)

    cols = ['mechanic', 'category', 'designer']
    data[cols].describe(include=np.object) \
              .transpose() \
              .to_csv(STATS_DIR+'factors.csv')

    # normalize and get stats from factors
    df_cat = norm_factor(data, 'category')
    df_mech = norm_factor(data, 'mechanic')

    counted_category = count_uniq(df_cat, 'category')
    counted_mechanic = count_uniq(df_mech, 'mechanic')

    plot_series(counted_category, 'category')
    plot_series(counted_mechanic, 'mechanic')

    counted_category.to_csv(STATS_DIR+'category.csv')
    counted_mechanic.to_csv(STATS_DIR+'mechanic.csv')

    # Plot
    # plot individual graphs

    plot_hist(data['avg_rating'], name='avg_rating')
    plot_hist(data['geek_rating'], name='geek_rating')
    plot_hist(data['num_votes'], name='num_votes', intervals='sqrt')
    plot_hist(data['owned'], name='owned', intervals='sqrt')

    # plot combined graph
    plot_hist(data['avg_rating'], name='', save=False)
    plot_hist(data['geek_rating'], name='Rating-vs-GRating', save=True,
              legend=['Avg_rating', 'Geek_rating'])


def plot_hist(narray, name, save=True,
              intervals='auto', legend=False):
    hist, bins = np.histogram(narray, bins=intervals)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    if not save:
        plt.figure(figsize=(12, 8))
    plt.bar(center, hist, align='center', width=width)
    plt.xlabel(name.capitalize())
    plt.ylabel('Frequency')
    if legend:
        plt.legend(legend)
    if save:
        plt.savefig(f"{IMG_DIR}{name}", dpi=200)
        plt.clf()


def plot_series(series, name, save=True):
    plt.figure(figsize=(20, 10))
    series.plot.bar()
    if save:
        plt.tight_layout()
        plt.savefig(f'{IMG_DIR}{name}', dpi=200)
        plt.clf()


def norm_factor(data, factor):
    df = []
    for row in data[factor]:
        entry = []
        for word in row.replace('/', ',').split(','):
            entry.append([word.strip().lower().replace('\'s', ''), 1])
        df.extend(entry)
    df = pd.DataFrame(df, columns=[factor, 'count'])
    return df


def count_uniq(data, factor):
    count = data[factor].apply(lambda x: pd.value_counts(x)).sum(axis=0)
    count = count.sort_values(ascending=False)
    return count


if __name__ == '__main__':
    main()
