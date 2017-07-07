from django.shortcuts import render
from django.http import HttpResponse

# This file contains the home page render.

def home(request):
    return render(request, 'home.html', {})
