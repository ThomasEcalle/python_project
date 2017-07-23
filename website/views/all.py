from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from ..models import Tournament, Group, Player, Participation, Node


@login_required
def all(request):
    """ this page will be needed to crete a tournament."""

    groups = Group.objects.filter(name=request.session['groupname'])
    tournaments = Tournament.objects.filter(group=groups[0])

    return render(request, 'all.html', locals())  # Show the subscription page.


@login_required
def infos(request, slug):
    """ used to print Tournament informations """
    if request.session.has_key('isAdmin'):
        isAdmin = True

    group = Group.objects.filter(name=request.session['groupname'])
    tournament = get_object_or_404(Tournament, name=slug, group=group)

    if tournament.isStarted:
        nodes = tournament.node_set.all().order_by('-rank')
        nodes = putNodesInTuples(nodes)
        ranks = getDifferentRanks(nodes)
        nodes_count = len(nodes)
        final_winner = getWinner(tournament)
        actual_rank = getActualRank(nodes)
        print("baaaaaaaaaaaaaaaaaaaaaaa : " + str(actual_rank))

    players_in_tournament = tournament.players.all()
    nb_players_in_tournament = len(players_in_tournament)
    players_remaining = Player.objects.filter(group=group)
    players_remaining = list(set(list(players_remaining)) - set(list(players_in_tournament)))

    return render(request, 'infos.html', locals())


@login_required
def add_player_in_tournament(request, slug):
    """ route in order to add one or several players in a tournament"""

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


@login_required
def remove_player_from_tournament(request, slug):
    """ route in order to remove one or several players of a tournament"""

    group = Group.objects.filter(name=request.session['groupname'])
    tournament = get_object_or_404(Tournament, name=slug, group=group)
    if request.POST:
        checkboxes = request.POST.getlist('player_box', '')
        for name in checkboxes:
            try:
                p = Player.objects.get(pseudo=name, group=group)
                participation = Participation.objects.get(player=p, tournament=tournament)
                participation.delete()
            except Player.DoesNotExist:
                print("impossible to get user from checkbox")
        return redirect(infos, slug=slug)


@login_required
def choose_winner(request):
    """ handle winner choixe """
    if request.POST:
        id_node = request.POST.get('winner', '')
        group = Group.objects.filter(name=request.session['groupname'])
        node = get_object_or_404(Node, pk=id_node)
        tournament = node.tournament
        try:
            player = node.player
            nodes = tournament.node_set.all()
            node_parent = node.parent
            node_parent.player = player
            node.winner = player
            node.save()
            node_parent.save()



        except Player.DoesNotExist:
            print("impossible to get user from radio button")
    return redirect(infos, tournament.name)


def putNodesInTuples(nodes):
    """ Help to transfer all the nodes into a Tuple list"""
    list = []
    for i, k in zip(nodes[0::2], nodes[1::2]):
        list.append((i, k))
    return list


def getDifferentRanks(nodes_tuple):
    """ Help us to get all the different ranks in tournament nodes"""
    list = []
    last = nodes_tuple[0][0].rank
    list.append(last)
    for t in nodes_tuple:
        rank = t[0].rank
        if rank != last:
            list.append(rank)
            last = rank
    return list


def getActualRank(nodes_tuple):
    """
        Help us to find the actual rank, in order to prevent
        the admi to set a match score before the one before.. my english is very well
        I'm actually writting this at 03:56 ...
    """
    list = getDifferentRanks(nodes_tuple)
    dict = {}
    already_done = []
    for rank in list:
        dict[rank] = True
    for node_tuple in nodes_tuple:
        if (node_tuple[0].parent.player is None or node_tuple[1].parent.player is None) and (node_tuple[0].player is not None and node_tuple[1].player is not None):
            dict[node_tuple[0].rank] = False

    print(dict)
    for k in dict:
        if dict[k] == True:
            already_done.append(k)
    max = 0
    for r in list:
        if r not in already_done and r > max:
            max = r

    return max


def getWinner(tournament):
    """ Method which return the winner if there is one"""
    try:
        final_node = tournament.node_set.get(rank=0)
    except Node.DoesNotExist:
        print("impossible to retrieve node from getWinner function")
    return final_node
