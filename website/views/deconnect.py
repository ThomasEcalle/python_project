from django.contrib.auth import logout
from django.shortcuts import redirect


# This file contains the deconnection handling page route.

def deconnect(request):
    """
        a deconnection link.
        Notice the CACHE element on settings.py.
        We added a dependancy in order to remove the dummy cache
        that can be an issue in order to process logout
    """
    print("yahoooooooooooo ")
    logout(request)
    return redirect('logon')
