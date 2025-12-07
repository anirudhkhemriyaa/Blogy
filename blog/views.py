from django.shortcuts import render , redirect
from .models import Blog , Category
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from blogy.forms import CategoryForm

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


def blogs(request , slug):
    single_blog = get_object_or_404(Blog , slug=slug , status="published")
    context = {
        'single_blog':single_blog,
    }
    return render(request , "blogs.html" , context)


# Searching ------ 
def search(request):
    keyword=request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains = keyword) | Q(short_description__icontains = keyword) | Q(blog_body__icontains = keyword) , status="published")
    context = {
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request , "search.html" , context)


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context ={
        'category_count':category_count,
        'blog_count':blogs_count

    }
    return render(request , "dashboard/dashboard.html" , context)



def categories(request):
    return render(request , 'dashboard/categories.html')



def add(request):
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form':form
    }
    return render(request , "dashboard/add_category.html" , context)