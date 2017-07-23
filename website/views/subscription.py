from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from ..forms import SubscriptionForm
from django.http import HttpResponse
from website.models import Group

# This file contains the subscription page route.

def subscription(request):

    # Load the subscription form with values entered by user if the form has been already submitted by user but incorrect else load it empty.
    form = SubscriptionForm(request.POST or None)

    # Check if form has been posted.
    if request.method == 'POST':

        # Check if form submitted by user is valid.
        if form.is_valid():

            # Try to get an account already using this name.
            try:

                account = Group.objects.get(name=form.cleaned_data.get('name'))

                # Inform user that the group name is already taken.
                messages.add_message(request, messages.ERROR, 'Ce nom de groupe n\'est pas disponible !')

            # The group does not exist, create a new one.
            except Group.DoesNotExist:

                # Create a new group object using data provided in form.
                new = Group(name=form.cleaned_data.get('name'), email=form.cleaned_data.get('email'), aPassword=form.cleaned_data.get('aPassword'), vPassword=form.cleaned_data.get('vPassword'))

                # Insert the new group in the database.
                new.save()

                # If the form is valid and can be submitted, return an information message to user.
                messages.add_message(request, messages.SUCCESS, 'Inscription effectuée !')

                # Form is submitted, redirect to the logon page.
                return redirect('/tournament/logon')

    # Show the subscription page.
    return render(request, 'subscription.html', locals())
