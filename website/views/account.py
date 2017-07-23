from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from website.models import Group

# This file contains the home page render.

def account(request):

    # Check if user is logged.
    if request.session.has_key('name'):

        # Check if user is an administrator before displaying the page.
        if request.session['admin'] == True:

            # Get account from database.
            group = Group.objects.get(name=request.session['name'])

            # Render the account page and send account data.
            return render(request, 'account.html', { 'name': group.name, 'email': group.email })

        # User is not an administrator, redirect him to the home page.
        else:

            messages.add_message(request, messages.WARNING, 'Vous devez être connecté en tant qu\'administrateur pour accéder à cette page !')
            return redirect('/tournament/home')

    # User is not logged, redirect to the logon page.
    else:

        messages.add_message(request, messages.WARNING, 'Vous devez être connecté pour accéder à cette page !')
        return redirect('/tournament/logon')
