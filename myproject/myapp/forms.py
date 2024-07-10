from django import forms
from .models import Blogs
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title','subtitle','description','image']

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Corfirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
