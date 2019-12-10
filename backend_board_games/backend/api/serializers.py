from rest_framework import serializers
from .models import Game, GameShort


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GameShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameShort
        fields = '__all__'
