from django import forms
from .models import Group

# Form used for subscription.

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
