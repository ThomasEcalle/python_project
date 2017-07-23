##################################################################

# Contains urls for the the website 'Tournament'

##################################################################

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^logon/', views.logon, name='logon'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^account/', views.account, name='account'),
    url(r'^subscription/', views.subscription, name='subscription'),
]
