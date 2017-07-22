from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ..forms import LogonForm
from ..models import Group

@login_required
def launch_tournament(request, slug):
	""" 
		Here is the algorithm in order to create a tournament
		We add a "final" to tournement, which can be seen like a binary tree.
		The  first one, set in the Model, is the final and got itself children until the 
		beginning of the tournament.
	"""
	if request.session.has_key('isConnected'):
		if request.session.has_key('isAdmin'):
		
			return redirect('home')
		else:
			return redirect('deconnect')
	else:
		return redirect('deconnect')
	
