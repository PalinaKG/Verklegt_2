from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from game.models import Game


def index(request):
    context = {'games': Game.objects.all()}
    return render(request, 'game/index.html', context)
