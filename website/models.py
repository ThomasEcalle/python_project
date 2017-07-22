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


class Participation(models.Model):
    """ Represent a link between Players and their different tournaments """
    player = models.ForeignKey('Player')
    tournament = models.ForeignKey('Tournament')

    def __str__(self):
        return "{0} participe au tournoi {1}".format(self.player.pseudo, self.tournament.name)
