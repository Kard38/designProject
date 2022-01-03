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
    gameplatform = get_object_or_404(Platform, games_id=id)

    context = {
        'game': game,
        'detail': gamedetail,
        'category': gamecategory,
        'platform': gameplatform,

    }
    return render(request, 'game/detail.html', context)


def game_cat(request):
    category = Category.objects.all()
    category = Category.objects.filter()

    context = {
        'game': category,
    }
    return render(request, 'game/category.html', context)


def user_favorite(request):
    current_user = request.user
    games = UsersFavorites.objects.filter(users=current_user)
    context = {
        'games': games,
    }
    return render(request, 'game/userfavorite.html', context)
