from django.contrib.auth.models import User
from django import forms


class SignUpForm(forms.ModelForm):
        class Meta:
            model = User
            fields = ['username', 'password', 'email', 'first_name', 'last_name']
