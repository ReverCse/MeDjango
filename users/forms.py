from django import forms
from django.contrib.auth.forms import UserCreationForm

class LogInForm(forms.Form):
    userID = forms.CharField(label='userID', max_length=100)
    password = forms.CharField(label='password')

class SignUpForm(forms.Form):
    username = forms.CharField(label='username')
    first_name = forms.CharField(label='first')
    last_name = forms.CharField(label='last')
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password')

