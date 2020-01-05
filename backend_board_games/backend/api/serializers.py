from rest_framework import serializers
from .models import Game, GameShort, SimilarGame, SimilarGameConnection, SimilarGameConnectionWeighted


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GameShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameShort
        fields = '__all__'


class SimilarGameSerializer(serializers.ModelSerializer):
    game = GameSerializer(read_only=True)
    rank = serializers.IntegerField(default=0)

    def create(self, validated_data):
        similar_game = SimilarGame(**validated_data)
        similar_game.save()
        return similar_game


class SimilarGameConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimilarGameConnection
        fields = '__all__'


class SimilarGameConnectionWeightedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimilarGameConnectionWeighted
        fields = '__all__'
