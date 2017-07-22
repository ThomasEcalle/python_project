from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import Tournament, Group, Player, Participation


# This file contains the players handling page route.
@login_required
def all(request):
    """ this page will be needed to crete a tournament."""
    
    groups = Group.objects.filter(name=request.session['groupname'])
    tournaments = Tournament.objects.filter(group=groups[0])

    return render(request, 'all.html', locals())  # Show the subscription page.

@login_required
def infos(request, slug):
    """ used to print Tournament informations """
    if request.session.has_key('isConnected'):
        group = Group.objects.filter(name=request.session['groupname'])
        tournament = get_object_or_404(Tournament, name=slug, group=group)

        players_in_tournament = tournament.players.all()
        players_remaining = Player.objects.filter(group=group)
        players_remaining = list(set(list(players_remaining)) - set(list(players_in_tournament)))

        return render(request, 'infos.html', locals())
    else:
        return redirect('deconnect', permanent=True)

@login_required
def add_player_in_tournament(request, slug):
    """ route in order to add one or several players in a tournament"""
    if request.session.has_key('isConnected'):
        group = Group.objects.filter(name=request.session['groupname'])
        tournament = get_object_or_404(Tournament, name=slug, group=group)
        if (request.POST):
            checkboxes = request.POST.getlist('player_box', '')
            for name in checkboxes:
                try:
                    p = Player.objects.get(pseudo=name, group=group)
                    Participation.objects.get_or_create(player=p, tournament=tournament)
                except Player.DoesNotExist:
                    print("impossible to get user from checkbox")
            return redirect(infos, slug=slug)
    else:
        return redirect('deconnect')

@login_required
def remove_player_from_tournament(request, slug):
    """ route in order to remove one or several players of a tournament"""
    if request.session.has_key('isConnected'):
        group = Group.objects.filter(name=request.session['groupname'])
        tournament = get_object_or_404(Tournament, name=slug, group=group)
        if (request.POST):
            checkboxes = request.POST.getlist('player_box', '')
            for name in checkboxes:
                try:
                    p = Player.objects.get(pseudo=name, group=group)
                    participation = Participation.objects.get(player=p, tournament=tournament)
                    participation.delete()
                except Player.DoesNotExist:
                    print("impossible to get user from checkbox")
            return redirect(infos, slug=slug)
    else:
        return redirect('deconnect')
