from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.category_name



class Blog(models.Model):
    Status_choices = [
        ('draft' , 'Draft'),
        ('published' , 'Publised'),
    ]
    title = models.CharField(max_length=100) 
    slug = models.SlugField(max_length=150 , unique=True , blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%y/%m/%d')
    short_description = models.TextField(max_length=200)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(choices=Status_choices , default=0)
    is_featured = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    



class about(models.Model):
    about_heading = models.CharField(max_length=50)
    about_description = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updates_at  = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "About"


    def __str__(self):
        return self.about_heading
    



class SocialLink(models.Model):
    plateform = models.CharField(max_length=25)
    link = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.plateform