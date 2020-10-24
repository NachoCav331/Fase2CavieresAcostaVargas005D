from django.shortcuts import render
from . models import Comic, Autor, Formato, Tipo
from django.views import generic

# Create your views here.

def index(request):
    comics = Comic.objects.all()

    return render(
        request, 
        'index.html', 
        context={'comics':comics}, 
    )
