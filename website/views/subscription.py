from django.contrib.auth.models import User
from django.shortcuts import render

from ..forms import SubscriptionForm


# This file contains the subscription page route.

def subscription(request):
    """ route in order to create a group
        We also define new USERS, one for the group and an other for the Player
    """
    # Load the subscription form with values entered by user if the form has been already submitted by user but incorrect else load it empty.


    form = SubscriptionForm(request.POST or None)  # Check if form has been posted.
    if request.method == 'POST':

        # Check if form submitted by user is valid.
        if form.is_valid():
            name = form.cleaned_data['name']
            adminPassword = form.cleaned_data['aPassword']
            visitorPassword = form.cleaned_data['vPassword']

            userAdmin = User.objects.create_user(username=name + "a", password=adminPassword)
            userVisitor = User.objects.create_user(username=name + "v", password=visitorPassword)

            userAdmin.save()
            userVisitor.save()
            # If the form is valid and can be submitted, return an information message to user.
            form.save()
            return render(request, 'logon.html', locals())  # Form is submitted, send a view with an empty form.

    return render(request, 'subscription.html', locals())  # Show the subscription page.
