from .models import Category , SocialLink

def geet_categories(request):
    return {"categories": Category.objects.all()}


def get_social(request):
    social = SocialLink.objects.all()
    return dict(social = social)