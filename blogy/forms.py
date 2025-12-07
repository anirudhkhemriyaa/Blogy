from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blog.models import  Category

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1','password2')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'