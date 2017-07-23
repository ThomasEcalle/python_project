import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from ..models import Group, Tournament, Node


@login_required
def launch_tournament(request, slug):
    """
        Here is the algorithm in order to create a tournament
        We add a "final" to tournement, which can be seen like a binary tree.
        The  first one, set in the Model, is the final and got itself children until the
        beginning of the tournament.
    """
    group = Group.objects.filter(name=request.session['groupname'])
    tournament = get_object_or_404(Tournament, name=slug, group=group)

    players_in_tournament = sorted(tournament.players.all().order_by('pseudo'), key=lambda x: random.random())

    rank = 0;

    # Here we set the Node that will represent our final node, our winner !
    tournament_final = Node(rank=rank, player=None, parent=None, tournament=tournament)
    tournament_final.save()

    matches = []

    matches.append(tournament_final)

    # looking for players that would make our tree not a perfect one
    tuple = getAdditionalPlayers(players_in_tournament)
    additionalPlayersCount = tuple[0]
    i = tuple[1]

    ugly_counter = [0]
    populate(tournament_final, rank, matches, players_in_tournament, i, additionalPlayersCount, ugly_counter);

    #printTree(matches)

    tournament.node_set = matches

    tournament.isStarted = True

    tournament.save()

    return redirect('infos', slug=tournament.name)


def printTree(matches):
    """ Used for debug, in order to print our binary tree"""
    for m in matches:
        print(m)


def getAdditionalPlayers(players):
    """ looks for 'additional users' that would make our tree not a perfect one """
    i = 0;
    additionalPlayersCount = 0;

    while 2 ** i <= len(players):
        additionalPlayersCount = len(players) - (2 ** i)
        i += 1
    if len(players) % 4 == 0 or len(players) == 2:
        additionalPlayersCount = 0;
        i -= 1

    return (additionalPlayersCount, i)


def populate(root, rank, matches, players, highestRank, additionalPlayersCount, ugly_counter):
    """
        Here is a reflexive method in order to populate our Tree.
        We have designated the HIGHEST rank possible before.
        So we juste have to create children to each Node "root".
    """
    if rank < highestRank:
        rank += 1
        match1 = Node(parent=root, rank=rank, player=None, tournament=root.tournament)

        if (rank == highestRank) or (additionalPlayersCount > 0 and rank == highestRank):
            if ugly_counter[0] < len(players):
                match1.player = players[ugly_counter[0]]
                ugly_counter[0] = ugly_counter[0] + 1
            additionalPlayersCount -= 1
        match1.save()
        matches.append(match1)

        match2 = Node(parent=root, rank=rank, player=None, tournament=root.tournament)
        if (rank == highestRank) or (additionalPlayersCount > 0 and rank == highestRank):
            if ugly_counter[0] < len(players):
                match2.player = players[ugly_counter[0]]
                ugly_counter[0] = ugly_counter[0] + 1
            additionalPlayersCount -= 1
        match2.save()
        matches.append(match2)

        populate(match1, rank, matches, players, highestRank, additionalPlayersCount, ugly_counter);
        populate(match2, rank, matches, players, highestRank, additionalPlayersCount, ugly_counter);
