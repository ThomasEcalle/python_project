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
]
