from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

# This file contains the home page render.

def home(request):
    if request.session.has_key('isConnected'):
        messages.add_message(request, messages.DEBUG, 'Test message !')
        return render(request, 'home.html', {})
    else:
        return redirect('logon', permanent=True)
