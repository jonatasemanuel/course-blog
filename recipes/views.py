from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {'name': 'Joetech'}
    return render(request, 'recipes/home.html', context)
