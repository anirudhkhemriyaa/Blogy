from django.shortcuts import render , redirect 
from django.http import HttpResponseRedirect
from .models import Blog , Category
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from blogy.forms import CategoryForm ,AddBlogg
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 
from .models import Comment
from django.core.paginator import Paginator


# Create your views here.

def post_by_category(request , category_id):
    posts = Blog.objects.filter(category = category_id  , status="published")

    paginator = Paginator(posts, 5) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    try:
        category = Category.objects.get(id=category_id)
    except:
        return redirect('home')
    context = {
        'posts':posts,
        'category':category,
        "page_obj": page_obj,

    }
    return render(request , "post_by_category.html" , context)


def blogs(request , slug):
    single_blog = get_object_or_404(Blog , slug=slug , status="published")
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = Comment.objects.filter(blog=single_blog).count()
    context = {
        'single_blog':single_blog,
        'comments':comments,
        'count':comment_count
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


@login_required
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.filter(author = request.user).count()
    context ={
        'category_count':category_count,
        'blog_count':blogs_count

    }
    return render(request , "dashboard/dashboard.html" , context)






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


def edit(request , pk):
    category = get_object_or_404(Category , pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST , instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context ={
        'form':form,
        'category':category,
    }
    return render(request , "dashboard/edit_cat.html", context)




def delete(request , pk):
    categ = get_object_or_404( Category, pk=pk)
    categ.delete()
    return redirect("categories")




def posts(request):
    posts = Blog.objects.filter(author=request.user)
    context = {
        'posts':posts
    }
    return render(request , "dashboard/posts.html" , context)



def add_blog(request):
    if request.method == "POST":
        form = AddBlogg(request.POST ,request.FILES )
        if form.is_valid():
            post = form.save(commit=False) # temp storing form
            post.author = request.user
            post.save() # we do it here for post id
            title = form.cleaned_data['title']
            post.slug=slugify(title) + '-'+str(post.id)
            post.save()
            return redirect('posts')
    form = AddBlogg()
    context = {
        'form':form
    }
    return render(request,"dashboard/add_blog.html" , context)



def edit_Post(request , pk):
    post = get_object_or_404(Blog , pk=pk)
    if request.method== 'POST':
        form = AddBlogg(request.POST , request.FILES , instance=post)
        if form.is_valid():
            post.save(commit=False)
            title=form.cleaned_data['title']
            post.slug=  slugify(title)+'-'+str(post.id)
            return redirect('posts')
    form = AddBlogg(instance=post)
    context ={
        'form':form,
        'post':post
    }
    return render(request, "dashboard/edit_post.html",context)


def delete_post(request  , pk ):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')

