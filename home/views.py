from django.shortcuts import render

# Create your views here.
import game.urls
import account.models


def home_view(request):
    gameurl = game.urls.game_index
    context = {
        'oyunlar': gameurl
    }
    return render(request, 'home.html', context)
