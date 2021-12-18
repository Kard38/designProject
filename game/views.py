from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def game_index(request):
    games = Games.objects.all()
    return render(request, 'game/index.html', {'games': games})


def game_detail(request, id):
    game = get_object_or_404(Games, GameId=id)
    gamedetail = get_object_or_404(GamesDetails, games_id=id)
    gamecategory = get_object_or_404(Category, games_id=id)
    context = {
        'game': game,
        'detail': gamedetail,
        'category': gamecategory,

    }
    return render(request, 'game/detail.html', context)
