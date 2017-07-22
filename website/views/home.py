from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    messages.add_message(request, messages.DEBUG, 'Test message !')
    return render(request, 'home.html', {})
