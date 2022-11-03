from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# HOME
def home(request):
    return render(request, 'recipes/home.html')


# CONTATO
def contato(request):
    return HttpResponse('contato')


# SOBRE
def sobre(request):
    return HttpResponse('sobre')
