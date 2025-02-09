from django import forms

from django.core import validators


class SignUpForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4)
    email = forms.EmailField(label="Enter your email", validators=[validators.validate_email])
    password = forms.CharField(label="Password", widget=forms.PasswordInput, min_length=8)
    re_password = forms.CharField(label='Re-enter Password', widget=forms.PasswordInput, min_length=8)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
