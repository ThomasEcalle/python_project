##################################################################

# Contains urls for the the website 'Tournament'

##################################################################

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^logon/', views.logon, name='logon'),
    url(r'^subscription/', views.subscription, name='subscription'),
    url(r'^players/', views.players, name='players'),
    url(r'^deconnect/', views.deconnect, name='deconnect'),
    url(r'^create_tournament/', views.create_tournament, name='create_tournament'),
    url(r'^all/', views.all, name='all'),
    url(r'^infos/(?P<slug>.+)', views.infos, name='infos'),
    url(r'^add_player_in_tournament/(?P<slug>.+)', views.add_player_in_tournament, name='add_player_in_tournament'),
    url(r'^remove_player_from_tournament/(?P<slug>.+)', views.remove_player_from_tournament, name='remove_player_from_tournament'),
    url(r'^launch_tournament/(?P<slug>.+)', views.launch_tournament, name='launch_tournament'),
    url(r'^choose_winner/', views.choose_winner, name='choose_winner'),
]
