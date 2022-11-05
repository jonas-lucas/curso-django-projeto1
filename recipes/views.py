from django.shortcuts import render

# Create your views here.


# HOME
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Jonas Lima',
    })
