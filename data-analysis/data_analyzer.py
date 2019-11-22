import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# rank, bgg_url, game_id, names, min_players, max_players, avg_time, min_time,
# max_time, year, avg_rating, geek_rating, num_votes, image_url, age, mechanic,
# owned, category, designer, weight

# Interesting ones
#  0 - rank
# 10 - avg_rating
# 11 - geek_rating
# 12 - num_votes
# 16 - owned

DATA_FILE = "board-game-data/bgg_db_1806.csv"
DIR = "data-analysis/"
NUM_STATS = DIR + "num_analysis.csv"
CAT_STATS = DIR + "cat_analysis.csv"
CAT_COUNT = DIR + "cat_count.csv"

def plot(narray, name, save=True, close=True, intervals="auto", legend=False):
    hist, bins = np.histogram(narray, bins=intervals)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.xlabel(name.capitalize())
    plt.ylabel("Frequency")
    if legend:
        plt.legend(legend)
    if save:
        plt.savefig(f"data-analysis/img/{name}")
    if close:
        plt.clf()

# read from file to pandas
data = pd.read_csv(DATA_FILE)
# data.info()

# save basic statistics
cols = ["avg_rating", "geek_rating", "num_votes", "owned", "min_players", "max_players", "avg_time", "min_time", "max_time"]
data[cols].describe().transpose().to_csv(NUM_STATS)


cols = ["mechanic", "category", "designer"]
data[cols].describe(include=np.object).transpose().to_csv(CAT_STATS)

# TODO refactor this
df_cat = []
for row in data['category']:
    entry = []
    for cat in row.replace('/',',').split(','):
        entry.append([cat.strip().lower().replace('\'s',''), 1])
    df_cat.extend(entry)
df_cat = pd.DataFrame(df_cat, columns=['category', 'count'])
print("Unique categories:",df_cat['category'].nunique())
print(df_cat["category"].describe(include=np.object))
cat_count = df_cat.category.apply(lambda x: pd.value_counts(x)).sum(axis = 0)
cat_count = cat_count.sort_values(ascending=False)
cat_count.plot.bar()
plt.savefig("data-analysis/img/category")
cat_count.to_csv(CAT_COUNT)


# Plot
# plot individual graphs
plot(data["avg_rating"], name="avg_rating")
plot(data["geek_rating"], name="geek_rating")
plot(data["num_votes"], name="num_votes", intervals="sqrt")
plot(data["owned"], name="owned", intervals="sqrt")

# plot combined graph
plot(data["avg_rating"], name="", save=False, close=False)
plot(data["geek_rating"], name="Rating-vs-GRating", save=True, close=True, legend=["Avg_rating", "Geek_rating"])
