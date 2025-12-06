from .models import Category

def geet_categories(request):
    category = Category.objects.all()
    return dict(category=category)
