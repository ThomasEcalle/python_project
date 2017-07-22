from django.contrib import messages
from django.shortcuts import render, redirect

from ..forms import PlayerForm
from ..models import Player


# This file contains the players handling page route.

def players(request):
    """ this page will be needed to crete users."""
    if request.session.has_key('isConnected'):

        if request.session.has_key('isAdmin'):
            isAdmin = request.session.has_key('isAdmin')

        form = PlayerForm(request.POST or None)  # Check if form has been posted.
        if request.method == 'POST':

            # Check if form submitted by user is valid.
            if form.is_valid():
                # If the form is valid and can be submitted, return an information message to user.
                pseudo = form.cleaned_data['pseudo']
                player = Player.objects.filter(pseudo=pseudo)
                if player:
                    messages.add_message(request, messages.ERROR, 'Ce pseudo est deja pris !')
                else:
                    form.save()
                    form = PlayerForm()
                    messages.add_message(request, messages.SUCCESS, pseudo + ' a bien ete ajoute!')

        players = Player.objects.all()
        return render(request, 'players.html', locals())  # Show the subscription page.

    else:
        return redirect('logon', permanent=True)
