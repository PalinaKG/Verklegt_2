from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


# Create your views here.
from game.models import Game


def index(request):
    context = {'games': Game.objects.all()}
    return render(request, 'game/index.html', context)


def get_game_by_id(request, id):
    return render(request, 'game/game_details.html', {
        'game': get_object_or_404(Game, pk=id)
    })