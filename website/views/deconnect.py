from django.shortcuts import render, redirect
# This file contains the deconnection handling page route.

def deconnect(request):
	print("yahoooooooooooo")
	for key in request.session.keys():
		del request.session[key]
		
	
