from .models import Picture
from  django import forms
from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

#from django.forms.widgets import PasswordInput, TextInput

class PicForm(forms.ModelForm):
    class Meta:
        model = Picture
        
        fields = ['title', 'my_pic', 'description', 'tag_category']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'give your picture a title'}),
            'description':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'give a description'}),
            'tag_category':forms.Select(choices=Picture.TAG_CATEGORY),
            
        }
                  
class DisplayForm(forms.ModelForm):
    class Meta:
        model = Picture

        fields = ['title','my_pic', 'description', 'tag_category']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'give your picture a title'}),
            'description':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'give a description'}),
            
            
        }
        

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

