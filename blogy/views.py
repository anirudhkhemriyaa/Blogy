from django.shortcuts import render , redirect
from blog.models import Category , Blog , about , SocialLink
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.core.paginator import Paginator


def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True).order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False , status='published')
    paginator = Paginator(posts, 5) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    try:
        About = about.objects.get()
    except:
        About = None

    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts':posts,
        'About':About,
        "page_obj": page_obj,

    }
    return render(request , "home.html" , context)


def log_out(request):
    logout(request)
    return redirect('home')