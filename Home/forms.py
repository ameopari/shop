from tkinter import Widget
from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='password1',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        label = {'email' : 'Email'}
        widget = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
     username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
     password = forms.CharField(label=_('password'),widget=forms.PasswordInput(attrs={'autocomplete':'current-Password','class':'form-control'}))
