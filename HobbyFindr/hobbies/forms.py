from django import forms
from django.core.validators import MinLengthValidator
from .models import *

class InputForm(forms.ModelForm):
    class Meta:
        model=Users
        fields = ['fname','lname','username','age','bio','city']
        labels = {
            "fname": "First Name",
            "lname": "Last Name",
            "username": "Username:",
            "bio": "Bio",
            "city": "City"
        }