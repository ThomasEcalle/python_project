from django.contrib import messages
from django.shortcuts import render

from ..forms import SubscriptionForm
from ..models import Group


# This file contains the subscription page route.

def subscription(request):
    # Load the subscription form with values entered by user if the form has been already submitted by user but incorrect else load it empty.
    form = SubscriptionForm(request.POST or None)

    # Check if form has been posted.
    if request.method == 'POST':

        # Check if form submitted by user is valid.
        if form.is_valid():
            # If the form is valid and can be submitted, return an information message to user.
            form.save()
            return render(request, 'subscripted.html', {})  # Form is submitted, send a view with an empty form.

    return render(request, 'subscription.html', locals())  # Show the subscription page.
