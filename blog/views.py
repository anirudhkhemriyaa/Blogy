from django.shortcuts import render , redirect
from .models import Blog , Category
# Create your views here.

def post_by_category(request , category_id):
    posts = Blog.objects.filter(category = category_id  , status="published")
    try:
        category = Category.objects.get(id=category_id)
    except:
        return redirect('home')
    context = {
        'posts':posts,
        'category':category
    }
    return render(request , "post_by_category.html" , context)