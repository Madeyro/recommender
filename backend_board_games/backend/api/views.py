from rest_framework.decorators import api_view
from .models import Game, GameShort, SimilarGame, SimilarGameConnection, SimilarGameConnectionWeighted
from .serializers import GameSerializer, GameShortSerializer, SimilarGameSerializer, SimilarGameConnectionSerializer
from rest_framework.response import Response
import random
import csv
import pandas
from six.moves import cPickle as pickle
import numpy as np
from itertools import chain
import re

def parse_data():
    DATA_SRC = './recommender/board-game-data/bgg_db_1806.csv'
    with open(DATA_SRC, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)
        for row in reader:
            _, new_game = GameShort.objects.get_or_create(
                rank=row[0],
                # bgg_url=row[1],
                # game_id=row[2],
                name=row[3],
                # min_players=row[4],
                # max_players=row[5],
                # avg_time=row[6],
                # min_time=row[7],
                # max_time=row[8],
                # year=row[9],
                # avg_rating=row[10],
                # geek_rating=row[11],
                # num_votes=row[12],
                image_url=row[13],
                # age=row[14],
                # mechanic=row[15],
                # owned=row[16],
                # category=row[17],
                # designer=row[18],
                # weight=row[19]
            )


def parse_games():
    DATA_SRC = './recommender/board-game-data/bgg_db_1806.csv'
    # Game.objects.all().delete()
    df = pandas.read_csv(DATA_SRC)
    for index, row in df.iterrows():
        game = Game()
        game.rank = row["rank"]
        game.bgg_url = row["bgg_url"]
        game.game_id = row["game_id"]
        game.names = row["names"]
        game.min_players = row["min_players"]
        game.max_players = row["max_players"]
        game.avg_time = row["avg_time"]
        game.min_time = row["min_time"]
        game.max_time = row["max_time"]
        game.year = row["year"]
        game.avg_rating = row["avg_rating"]
        game.geek_rating = row["geek_rating"]
        game.num_votes = row["num_votes"]
        game.image_url = row["image_url"]
        game.age = row["age"]
        game.mechanic = row["mechanic"]
        game.owned = row["owned"]
        game.category = row["category"]
        game.designer = row["designer"]
        game.weight = row["weight"]
        game.save()


def read_matrices():
    objects = []
    # with (open("/Users/darigummy/Downloads/matrices/uw_matrix.pickle", "rb")) as openfile:
    #     while True:
    #         try:
    #             # objects.append(pickle.load(openfile))
    #             objects = pickle.load(openfile)
    #             # print(pickle.load(openfile))
    #             print(objects[1])
    #
    #         except EOFError:
    #             break
    #         openfile.close()
    infile = open("./recommender/board-game-data/matrices/uw_matrix.pickle", "rb")
    data = pickle.load(infile, encoding='latin1')
    infile.close()
    print('Showing the pickled data:')
    with open("./recommender/board-game-data/matrices/uw_matrix.txt", "w") as file:
        for key, value in data.items():
            line = 'The game ' + str(key) + ' similar games are ' + str(value)
            # similar_game = SimilarGame()
            # similar_game.game = key
            # similar_game.rank = value
            # similar_game.save()
            # file.write(line)
            connection = SimilarGameConnection()
            connection.game_rank = key
            connection.similar_games_rank = value
            connection.save()
            file.write(line)


def read_matrices_weighted():
    objects = []
    # with (open("/Users/darigummy/Downloads/matrices/uw_matrix.pickle", "rb")) as openfile:
    #     while True:
    #         try:
    #             # objects.append(pickle.load(openfile))
    #             objects = pickle.load(openfile)
    #             # print(pickle.load(openfile))
    #             print(objects[1])
    #
    #         except EOFError:
    #             break
    #         openfile.close()
    infile = open("./recommender/board-game-data/matrices/w_matrix.pickle", "rb")
    data = pickle.load(infile, encoding='latin1')
    infile.close()
    print('Showing the pickled data:')
    with open("./recommender/board-game-data/matrices/w_matrix.txt", "w") as file:
        for key, value in data.items():
            line = 'The game ' + str(key) + ' similar games are ' + str(value)
            # similar_game = SimilarGame()
            # similar_game.game = key
            # similar_game.rank = value
            # similar_game.save()
            # file.write(line)
            connection = SimilarGameConnectionWeighted()
            connection.game_rank = key
            connection.similar_games_rank = value
            connection.save()
            file.write(line)


@api_view(['GET'])
def ten_random_games(request):
    # parse_data()
    # read_matrices_weighted()
    # read_matrices()
    if request.method == 'GET':
        games = GameShort.objects.all()
        random_games = random.sample(list(games), 10)
        serializer = GameShortSerializer(random_games, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def ten_random_games_full(request):
    # parse_games()
    if request.method == 'GET':
        games = Game.objects.all()
        random_games = random.sample(list(games), 10)
        serializer = GameSerializer(random_games, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def game_detail(request, pk):
    try:
        game = Game.objects.get(rank=pk)
        game_rank = SimilarGameConnection(game_rank=pk)
    except Game.DoesNotExist as error:
        return Response({"error": str(error)})
    except SimilarGameConnection.DoesNotExist as error:
        return Response({"error": str(error)})
    if request.method == 'GET':
        random_games = Game.objects.all()
        random_games_ten_1 = random.sample(list(random_games), 6)

        similar_games_unweighted = SimilarGameConnection.objects.filter(game_rank=pk).values_list(
            'similar_games_rank', flat=True)
        result_ranks_unweighted = []
        for value in similar_games_unweighted:
            ranks = value[1:len(value)-1]
            # res = [int(i) for i in test_string.split() if i.isdigit()]
            result_ranks_unweighted = re.findall(r'\b\d+\b', ranks)
        # print(result_ranks_unweighted)
        result_array_unweighted = []
        for result_rank in result_ranks_unweighted:
            result_array_unweighted.append(Game.objects.get(rank=result_rank))
        # print(result_array_unweighted)

        similar_games_ten_weighted = SimilarGameConnectionWeighted.objects.filter(game_rank=pk).values_list(
            'similar_games_rank', flat=True)
        result_ranks_weighted = []
        for value in similar_games_ten_weighted:
            ranks_weighted = value[1:len(value) - 1]
            result_ranks_weighted = re.findall(r'\b\d+\b', ranks_weighted)
        # print(result_ranks_weighted)
        result_array_weighted = []
        for result_ranks_weighted in result_ranks_weighted:
            result_array_weighted.append(Game.objects.get(rank=result_ranks_weighted))
        # print(result_array_weighted)

        game_serializer = GameSerializer(game)
        games_serializer_1 = GameSerializer(random_games_ten_1, many=True)
        games_serializer_2 = GameSerializer(result_array_unweighted[0:6], many=True)
        games_serializer_3 = GameSerializer(result_array_weighted[6:12], many=True)
        return Response({'game_detail': game_serializer.data, 'random_games_1': games_serializer_1.data,
                         'result_array_unweighted': games_serializer_2.data, 'result_array_weighted': games_serializer_3.data})
