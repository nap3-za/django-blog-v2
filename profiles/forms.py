from django import forms
from django.contrib.auth.models import User

class RegForm(forms.Form):
    username = forms.CharField(max_length=300)
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Pick another username")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Invalid email")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(max_length=300)
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid user")
        return username