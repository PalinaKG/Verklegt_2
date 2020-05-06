from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from console.models import Console


# Create your views here.
def index(request):
    context = {'consoles': Console.objects.all()}
    return render(request, 'console/index.html', context)


def get_console_by_id(request, id):
    return render(request, 'console/console_details.html', {
        'console': get_object_or_404(Console, pk=id)
    })
