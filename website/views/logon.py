from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from ..forms import LogonForm
from ..models import Group

# This file contains the logon page render.
def logon(request):

    # Check if user is already logged.
    if request.session.has_key('name'):

        # User is already logged, redirect him to the home page.
        messages.add_message(request, messages.INFO, 'Vous êtes déjà connecté !')
        return redirect('/tournament/home')

    # User is not logged, redirect to the logon page.
    else:

        # Check if the server is in production or not.
        if settings.ENVIRONMENT != 'PROD':

            # Print an information message saying in wich environment the server is for now.
            messages.add_message(request, messages.INFO, 'Environnement is ' + settings.ENVIRONMENT + ' !')

        # Check if debug mode is on.
        if settings.DEBUG == True:

            # Print a warning message to inform that the debug mode is on.
            messages.add_message(request, messages.WARNING, 'Debug mode is ON !')

            # Put the logon form on the view.
        form = LogonForm(request.POST or None)

        # Check if form has been posted.
        if request.method == 'POST':

            # Check if form submitted by user is valid.
            if form.is_valid():

                # Try to find an admin account using credentials.
                try:
                    results = Group.objects.get(name=form.cleaned_data['name'], aPassword=form.cleaned_data['password'])

                    # Store group name in session, by this way we can check is user is logged by checking if there is a name in session.
                    request.session['name'] = form.cleaned_data['name']

                    # Precise that logged user is an administrator.
                    request.session['admin'] = True

                    # Group found, return a success message.
                    messages.add_message(request, messages.SUCCESS, 'Vous êtes maintenant connecté en tant qu\'administrateur !')

                    # Redirect user to home page.
                    return redirect('home', permanent=True)

                # No group found using these credentials.
                except Group.DoesNotExist:

                    # Try to find a visitor group using these credentials.
                    try:
                        results = Group.objects.get(name=form.cleaned_data['name'], vPassword=form.cleaned_data['password'])

                        # Store group name in session, by this way we can check is user is logged by checking if there is a name in session.
                        request.session['name'] = form.cleaned_data['name']

                        # Precise that logged user is not an administrator.
                        request.session['admin'] = False

                        # Group found, return a success message.
                        messages.add_message(request, messages.SUCCESS, 'Vous êtes maintenant connecté en tant que visiteur !')

                        # Redirect user to home page.
                        return redirect('home')

                    # No group found using the visitor password.
                    except Group.DoesNotExist:

                        # Return an error message.
                        messages.add_message(request, messages.ERROR, 'Identifiant ou mot de passe incorrect !')

        return render(request, 'logon.html', locals())
