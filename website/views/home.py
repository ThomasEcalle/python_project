from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse

# This file contains the home page render.

def home(request):
    messages.add_message(request, messages.DEBUG, 'Test message !')
    return render(request, 'home.html', {})
