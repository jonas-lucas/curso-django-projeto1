from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# HOME
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Jonas Lima',
    })


# CONTATO
def contato(request):
    return render(request, 'recipes/contato.html')


# SOBRE
def sobre(request):
    return HttpResponse('sobre')
