from django.shortcuts import render
from blog.models import Category , Blog , about , SocialLink

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