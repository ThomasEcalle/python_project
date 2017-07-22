from django.contrib import messages
from django.shortcuts import render, redirect

from ..forms import TournamentForm
from ..models import Tournament, Group


# This file contains the players handling page route.

def create_tournament(request):
    """ this page will be needed to crete a tournament."""
    if request.session.has_key('isConnected'):
        groups = Group.objects.filter(name=request.session['groupname'])
        group = groups[0]
        if request.session.has_key('isAdmin'):
            form = TournamentForm(request.POST or None)  # Check if form has been posted.
            if request.method == 'POST':

                # Check if form submitted by user is valid.
                if form.is_valid():
                    # If the form is valid and can be submitted, return an information message to user.
                    name = form.cleaned_data['name']
                    tournament = Tournament.objects.filter(name=name, group=group)
                    if tournament:
                        messages.add_message(request, messages.ERROR, 'Un tournoi porte deja ce nom')
                    else:
                        tournament = form.save(commit=False)
                        tournament.isStarted = False
                        tournament.group = group

                        tournament.save()
                        return redirect('all', permanent=True)

            return render(request, 'create_tournament.html', locals())  # Show the subscription page.

        else:
            return redirect('deconnect', permanent=True)

    else:
        return redirect('deconnect', permanent=True)
