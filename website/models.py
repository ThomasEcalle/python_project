from django.db import models


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nom Du Groupe")
    email = models.EmailField(max_length=128, verbose_name="Adresse Email Du Groupe")
    aPassword = models.CharField(max_length=64, verbose_name="Mot De Passe Administrateur")
    vPassword = models.CharField(max_length=128, verbose_name="Mot De Passe Visiteur")

    def __str__(self):
        return 'Group name : ' + self.name + ' | Group email : ' + self.email


class Player(models.Model):
    pseudo = models.CharField(max_length=64, verbose_name="Pseudo")

    def __str__(self):
        return self.pseudo


class Tournament(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nom du tournoi")
    isStarted = models.BooleanField(verbose_name="commence")

    def __str__(self):
        return self.name