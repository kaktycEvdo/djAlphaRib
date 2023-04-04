from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class AboutForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass


class AuthForm(AuthenticationForm):
    login = forms.EmailField(widget=forms.EmailInput, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=50)

    class Meta:
        model = User
        fields = ['email', 'password']


class RegForm(forms.ModelForm):
    login = forms.EmailField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=50)

    class Meta:
        model = User
        fields = ['login', 'password']
