from typing import Any
from django import forms

from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"placeholder": "Enter username"})
        self.fields["email"].widget.attrs.update({"placeholder": "Enter email"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Enter password"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Enter confirm password"})


class CustomAuthenticationForm(AuthenticationForm):
    # email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"placeholder": "Enter email"})
        self.fields["password"].widget.attrs.update({"placeholder": "Enter password"})