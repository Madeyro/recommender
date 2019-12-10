from rest_framework.decorators import api_view
from .models import Game, GameShort
from .serializers import GameSerializer, GameShortSerializer
from rest_framework.response import Response
import random
import csv
import pandas


def parse_data():
    DATA_SRC = '/Users/darigummy/Desktop/board-game-data/bgg_db_1806.csv'
    with open(DATA_SRC, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)
        for row in reader:
            _, new_game = GameShort.objects.get_or_create(
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
    DATA_SRC = '/Users/darigummy/Desktop/board-game-data/bgg_db_1806.csv'
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

@api_view(['GET'])
def ten_random_games(request):
    # parse_data()
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

