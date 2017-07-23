from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from django.shortcuts import render

from ..forms import LogonForm
from ..models import Group, Tournament


# This file contains the logon page render.
def logon(request):
    """ Login work """
    # Check if the server is in production or not.
    # if settings.ENVIRONMENT != 'PROD':
        # Print an information message saying in wich environment the server is for now.
        #messages.add_message(request, messages.INFO, 'Environnement is ' + settings.ENVIRONMENT + ' !')

    # Check if debug mode is on.
	# if settings.DEBUG == True:
		# Print a warning message to inform that the debug mode is on.
		# messages.add_message(request, messages.WARNING, 'Debug mode is ON !')

    # Put the logon form on the view.
    form = LogonForm(request.POST or None)

    # Check if form has been posted.
    if request.method == 'POST':

        # Check if form submitted by user is valid.
        if form.is_valid():

            user = authenticate(username=form.cleaned_data['name'] + "a", password=form.cleaned_data['password'])
            if user:
                needPermission = True
            if user is None:
                user = authenticate(username=form.cleaned_data['name'] + "v", password=form.cleaned_data['password'])
                needPermission = False
            if user is not None:
                # Try to find an admin account using credentials.
                login(request, user)
                if needPermission:
                    content_type = ContentType.objects.get_for_model(Tournament)
                    permission = Permission.objects.get(content_type=content_type, codename='modify_tournament')
                    user.user_permissions.add(permission)

                try:
                    results = Group.objects.get(name=form.cleaned_data['name'], aPassword=form.cleaned_data['password'])
                    # Group found, return a success message.
                    messages.add_message(request, messages.SUCCESS,
                                         'Vous êtes maintenant connecté en tant qu\'administrateur !')  # Redirect user to home page.

                    request.session["groupname"] = results.name
                    request.session["isAdmin"] = True
                    return redirect('home')

                # No group found using these credentials.
                except Group.DoesNotExist:  # Try to find a visitor group using these credentials.
                    try:
                        results = Group.objects.get(name=form.cleaned_data['name'],
                                                    vPassword=form.cleaned_data['password'])

                        # Group found, return a success message.
                        messages.add_message(request, messages.SUCCESS,
                                             'Vous êtes maintenant connecté en tant que visiteur !')

                        request.session["groupname"] = results.name
                        # Redirect user to home page.
                        return redirect('home')

                    # No group found using the visitor password.
                    except Group.DoesNotExist:

                        # Return an error message.
                        messages.add_message(request, messages.ERROR, 'Identifiant ou mot de passe incorrect !')
            else:
                messages.add_message(request, messages.ERROR, 'Identifiant ou mot de passe incorrect !')
        return render(request, 'logon.html', locals())
    return render(request, 'logon.html', locals())
