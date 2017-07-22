from django.shortcuts import render, redirect
from django.contrib.auth import logout
# This file contains the deconnection handling page route.

def deconnect(request):
	print("yahoooooooooooo ")
	logout(request)
	return redirect('logon', permanent=True)
	
