from django.contrib import admin
from .models import Game, GameShort, SimilarGameConnection, SimilarGameConnectionWeighted

admin.site.register(Game)
admin.site.register(GameShort)
admin.site.register(SimilarGameConnection)
admin.site.register(SimilarGameConnectionWeighted)