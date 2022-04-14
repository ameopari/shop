from tkinter import Widget
from django.core import validators
from django import forms
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
# from django.utils.translation import gettext,gettext_lazy as _

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

# class LoginForm(AuthenticationForm):
#      username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
#      password = forms.CharField(label=_('password'),widget=forms.PasswordInput(attrs={'autocomplete':'current-Password','class':'form-control'}))

# {% load static %}

# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
# <div class="container">
#  <div class="row my-3">
#   <div class="col-sm-6 offset-sm-3">
#    <h3>Login</h3>
#    <hr>
#    <form action="" method="post" novalidate class="shadow p-5">
#        {% csrf_token %}
#        {% for fm in form %}
#        <div class="form-group">
#         {{fm.label_tag}} {{fm}} <small class="text-danger">{{fm.errors|striptags}}</small>
#         </div>
#         {% endfor %}
#         {% comment %} <small><a href="{% url 'password-reset' %}">forgot password ?</a></small><br> {% endcomment %}
#         <input type="submit" class="btn btn-primary mt-4" value="login">
#         <br>
#         <div class="text-center text primary fw-bold"><small>New To Shopping ?<a href="{% url 'register' %}" class="text-danger">Create an Account</a></small></div>
#         {% if form.non_field.errors %}
#         {% for error in form.non_field.errors %}
#         <p class="alert alert-danger my-3">{{error}}</p>
#         {% endfor %}
#         {% endif %}
#                </form>
#              </div>
#              <div class="modal-footer">
#                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
#                <button type="button" class="btn btn-primary">Send message</button>
#              </div>
#            </div>
#          </div>
#        </div>
