from django.db import models


# Create your models here.

class Group(models.Model):
    """ Represent a group (a compagny, a group of friends... un troupeau de banane !) """
    name = models.CharField(max_length=64, verbose_name="Nom Du Groupe")
    email = models.EmailField(max_length=128, verbose_name="Adresse Email Du Groupe")
    aPassword = models.CharField(max_length=64, verbose_name="Mot De Passe Administrateur")
    vPassword = models.CharField(max_length=128, verbose_name="Mot De Passe Visiteur")

    def __str__(self):
        return self.name


class Player(models.Model):
    """ Represent a player """
    pseudo = models.CharField(max_length=64, verbose_name="Pseudo")
    group = models.ForeignKey('Group')

    def __str__(self):
        return self.pseudo


class Tournament(models.Model):
    """ Represent a tournament """
    name = models.SlugField(max_length=64, verbose_name="Nom du tournoi")
    isStarted = models.BooleanField(verbose_name="commence")
    group = models.ForeignKey('Group')
    players = models.ManyToManyField(Player, through='Participation')

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ("modify_tournament", "enable user to modify everything about a tournament"),
        )


class Node(models.Model):
    """ Represent a Node of the binary tree's tournament """
    rank = models.IntegerField()
    parent = models.ForeignKey('Node', null=True)
    player = models.ForeignKey('Player', null=True, related_name='player')
    winner = models.ForeignKey('Player', null=True, related_name='winner')
    tournament = models.ForeignKey('Tournament')

    def __str__(self):
        name = self.player.pseudo if self.player is not None else "0"
        parent_id = self.parent.id if self.parent is not None else "none"
        return "Node (" + self.tournament.name + ") id: " + str(self.id) + ",  rank : " + str(
            self.rank) + ", player = " + name + ", parent : " + str(parent_id)


class Participation(models.Model):
    """ Represent a link between Players and their different tournaments """
    player = models.ForeignKey('Player')
    tournament = models.ForeignKey('Tournament')

    def __str__(self):
        return "{0} participe au tournoi {1}".format(self.player.pseudo, self.tournament.name)
