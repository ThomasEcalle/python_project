from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse

# This file contains the home page render.

def logon(request):
    messages.add_message(request, message.INFO, 'Vous pouvez utiliser le mot de passe administrateur ou le mot de passe visiteur')
    return render(request, 'logon.html', {})
