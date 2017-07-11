from django import forms
from .models import Group
from django.contrib import messages

###############################################################################################################################################

# Form used for subscription.
class SubscriptionForm(forms.ModelForm):

    # Set the field as password in the form to hide the text from the input.
    aPassword = forms.CharField(widget=forms.PasswordInput(), label='Mot De Passe Administrateur')
    vPassword = forms.CharField(widget=forms.PasswordInput(), label='Mot De Passe Visiteur')

    # Create confirmation input for passwords.
    aConfirm = forms.CharField(widget=forms.PasswordInput(), label='Confirmation')
    vConfirm = forms.CharField(widget=forms.PasswordInput(), label='Confirmation')

    # Create the form using the 'group' model.
    class Meta:
        model = Group
        fields = ('name', 'email', 'aPassword', 'aConfirm', 'vPassword', 'vConfirm')

    # Defined custom 'clean' function in order to check password confirmations.
    def clean(self):

        # Apply the default cleaning function before checking passwords.
        cleaned_data = super(SubscriptionForm, self).clean()

        # Get administration password and its confirmation in variables.
        aPassword = cleaned_data.get('aPassword')
        aConfirm = cleaned_data.get('aConfirm')

        # Get visit password and its confirmation in variables.
        vPassword = cleaned_data.get('vPassword')
        vConfirm = cleaned_data.get('vConfirm')

        # Raise an error if the administration password and its confirmation do not match.
        if aPassword != aConfirm:
            raise forms.ValidationError('Le mot de passe d\'administration et sa confirmation sont différents !')

        # Raise an error if the visitor password and its confirmation do not match.
        if vPassword != vConfirm:
            raise forms.ValidationError('Le mot de passe visiteur et sa confirmation sont différents !')

###############################################################################################################################################

# Logon form.
class LogonForm(forms.Form):

    name = forms.CharField(required=True, label='Nom Du Groupe')
    password = forms.CharField(required=True, widget=forms.PasswordInput(), label='Mot De Passe')

###############################################################################################################################################
