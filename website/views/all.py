from django.shortcuts import render, redirect

from ..models import Tournament


# This file contains the players handling page route.

def all(request):
    """ this page will be needed to crete a tournament."""
    if request.session.has_key('isConnected'):
        tournaments = Tournament.objects.all()

        return render(request, 'all.html', locals())  # Show the subscription page.

    else:
        return redirect('deconnect', permanent=True)
