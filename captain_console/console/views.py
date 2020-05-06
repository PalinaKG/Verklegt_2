from django.shortcuts import render
from django.http import HttpResponse
from console.models import Console


# Create your views here.
def index(request):

    context= {'consoles': Console.objects.all()}
    return render(request, 'console/index.html',context)