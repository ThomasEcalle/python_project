from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import PlayerForm
from ..models import Player, Group


# This file contains the players handling page route.
@login_required
def players(request):
    """ this page will be needed to crete users."""
    if request.session.has_key('isAdmin'):
        isAdmin = True
    form = PlayerForm(request.POST or None)  # Check if form has been posted.
    groups = Group.objects.filter(name=request.session['groupname'])
    group = groups[0]
    if request.method == 'POST':

        # Check if form submitted by user is valid.
        if form.is_valid():
            # If the form is valid and can be submitted, return an information message to user.
            pseudo = form.cleaned_data['pseudo']
            player = Player.objects.filter(pseudo=pseudo, group=group)
            if player:
                messages.add_message(request, messages.ERROR, 'Ce pseudo est deja pris !')
            else:
                playerObject = form.save(commit=False)
                try:
                    group = Group.objects.get(name=request.session['groupname'])
                    playerObject.group = group
                    playerObject.save()
                    form = PlayerForm()
                    messages.add_message(request, messages.SUCCESS, pseudo + ' a bien ete ajoute!')

                except Group.DoesNotExist:
                    return redirect('deconnect')

    players = Player.objects.filter(group=group)
    return render(request, 'players.html', locals())  # Show the subscription page.
