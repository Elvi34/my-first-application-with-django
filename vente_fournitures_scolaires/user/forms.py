
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(forms.ModelForm):
    
    role = forms.ChoiceField(
        choices=[('client', 'Client')],
        widget=forms.HiddenInput(),
        initial='client'
    )


