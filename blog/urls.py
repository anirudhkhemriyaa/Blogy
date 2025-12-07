from django.urls import path , include
from . import views

urlpatterns = [
    path('<int:category_id>/', views.post_by_category , name="post_by_category"),
    path('', views.dashboard , name="dashboard"),
    path('categories/', views.categories , name="categories"),
    path('categories/add', views.add , name="add"),
    # path('categories/delete', views.delete , name="delete"),

]
