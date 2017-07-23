from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

# This file contains the home page render.

def home(request):

    # Check if user is logged before displaying the page.
    if request.session.has_key('name'):

        messages.add_message(request, messages.DEBUG, 'Test message !')
        return render(request, 'home.html', { 'name': request.session['name'] })

    # User is not logged, redirect to the logon page.
    else:

        return redirect('/tournament/logon')
