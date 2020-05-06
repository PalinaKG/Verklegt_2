from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from manufacturer.models import Manufacturer


def index(request):
    context = {'manufacturers': Manufacturer.objects.all()}
    return render(request, 'manufacturer/index.html', context)