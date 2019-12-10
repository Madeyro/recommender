from django.urls import path
from .views import *

urlpatterns = [
    path('games_short', ten_random_games),
    path('games_full', ten_random_games_full),
    path('games_full/<int:pk>/', game_detail),
]
