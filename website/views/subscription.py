from django.shortcuts import render
from django.http import HttpResponse

# This file contains the subscription page route.

def subscription(request):
    return render(request, 'subscription.html', {})
