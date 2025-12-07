from django.shortcuts import render , redirect
from blog.models import Category , Blog , about , SocialLink
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout



def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False , status='published')
    try:
        About = about.objects.get()
    except:
        About = None

    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts':posts,
        'About':About,

    }
    return render(request , "home.html" , context)



def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('home')
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request , "register.html" , context)




def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request , request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username = username , password=password)
            if user is not None:
                login(request , user)
                return redirect('dashboard')
            else:
                return redirect('login')

    form = AuthenticationForm()
    context ={
        'form':form
    }
    return render(request , "login.html" , context)



def log_out(request):
    logout(request)
    return redirect('home')