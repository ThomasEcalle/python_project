from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

# This file ends current session.

def logout(request):

    # Check if user is logged before displaying the page.
    if request.session.has_key('name'):

        # End user's session.
        request.session.flush()

        messages.add_message(request, messages.INFO, 'Vous êtes maintenant déconnecté !')
        return redirect('/tournament/logon')

    # User is not logged, redirect to the logon page.
    else:

        messages.add_message(request, messages.WARNING, 'Vous devez être connecté pour mettre fin à votre session !')
        return redirect('/tournament/logon')
