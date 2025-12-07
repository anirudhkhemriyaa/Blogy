from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from blog.models import  Category , Blog

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1','password2')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'



class AddBlogg(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title' ,'category' ,'featured_image', 'short_description' ,'blog_body' , 'status' ,'is_featured')