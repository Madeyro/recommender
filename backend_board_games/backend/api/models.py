from django.db import models


class Game(models.Model):
    class Meta:
        verbose_name = 'Game Full'
        verbose_name_plural = 'Games Full'

    rank = models.PositiveIntegerField(default=0)
    bgg_url = models.CharField(max_length=700, blank=True, null=True)
    game_id = models.CharField(max_length=700, blank=True, null=True)
    names = models.CharField(max_length=700, blank=True, null=True)
    min_players = models.IntegerField(default=1)
    max_players = models.IntegerField(default=4)
    avg_time = models.IntegerField(default=30)
    min_time = models.IntegerField(default=30)
    max_time = models.IntegerField(default=30)
    year = models.IntegerField(default=1998)
    avg_rating = models.FloatField(default=0)
    geek_rating = models.FloatField(default=0)
    num_votes = models.IntegerField(default=0)
    image_url = models.CharField(max_length=700, blank=True, null=True)
    age = models.IntegerField(default=0)
    mechanic = models.CharField(max_length=700, blank=True, null=True)
    owned = models.IntegerField(default=0)
    category = models.CharField(max_length=700, blank=True, null=True)
    designer = models.CharField(max_length=700, blank=True, null=True)
    weight = models.FloatField(default=0)

    def __str__(self):
        return self.names


class GameShort(models.Model):
    class Meta:
        verbose_name = 'Game Short'
        verbose_name_plural = 'Games Short'

    rank = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=200, blank=False, null=True)
    image_url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class SimilarGame(models.Model):
    class Meta:
        verbose_name = 'Similar Game'
        verbose_name_plural = 'Similar Games'

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='games')
    ranks = models.PositiveIntegerField(default=0)


class SimilarGameConnection(models.Model):
    class Meta:
        verbose_name = 'Connection Unweighted'
        verbose_name_plural = 'Connections Unweighted'

    game_rank = models.IntegerField(default=0)
    similar_games_rank = models.CharField(max_length=500, blank=True, null=True)
    # similar_games_rank = models.IntegerField(default=0)

    def __str__(self):
        return str(self.game_rank)


class SimilarGameConnectionWeighted(models.Model):
    class Meta:
        verbose_name = 'Connection Weighted'
        verbose_name_plural = 'Connections Weighted'

    game_rank = models.IntegerField(default=0)
    similar_games_rank = models.CharField(max_length=500, blank=True, null=True)
    # similar_games_rank = models.IntegerField(default=0)

    def __str__(self):
        return str(self.game_rank)
