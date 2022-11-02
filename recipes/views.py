from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# HOME
def home(request):
    return HttpResponse('HOME')


# CONTATO
def contato(request):
    return HttpResponse('contato')


# SOBRE
def sobre(request):
    return HttpResponse('sobre')
