from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

# Create your views here.
from game.models import Game


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']

        games = [{
            'id': x.id,
            'name': x.name,
           'description': x.description,
            'firstImage': x.gameimage_set.first().image

        } for x in Game.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': games})
    context = {'games': Game.objects.all().order_by('name')}
    return render(request, 'homepage/index.html', context)


def get_game_by_id(request, id):
    return render(request, 'game/game_details.html', {
        'game': get_object_or_404(Game, pk=id)
    })