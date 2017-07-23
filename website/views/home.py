from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    """ show a basic home page"""
    # messages.add_message(request, messages.DEBUG, 'Test message !')
    return render(request, 'home.html', {})
