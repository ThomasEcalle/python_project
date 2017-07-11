from django.shortcuts import render
from django.contrib import messages
from ..forms import SubscriptionForm
from django.http import HttpResponse

# This file contains the subscription page route.

def subscription(request):

    # Load the subscription form with values entered by user if the form has been already submitted by user but incorrect else load it empty.
    form = SubscriptionForm(request.POST or None)

    # Check if form has been posted.
    if request.method == 'POST':

        # Check if form submitted by user is valid.
        if form.is_valid():

            # If the form is valid and can be submitted, return an information message to user.
            messages.add_message(request, messages.SUCCESS, 'Inscription effectuée !')

            # Form is submitted, send a view without the form.
            return render(request, 'subscripted.html', {})

    # Show the subscription page.
    return render(request, 'subscription.html', locals())
