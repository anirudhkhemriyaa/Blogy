from django.urls import path , include
from . import views

urlpatterns = [
    path('<int:category_id>/', views.post_by_category , name="post_by_category"),
    path('', views.dashboard , name="dashboard"),
    path('categories/', views.categories , name="categories"),
    path('categories/add', views.add , name="add"),
    path('categories/edit/<int:pk>/', views.edit , name="edit"),
    path('categories/delete/<int:pk>/', views.delete , name="delete"),
    path('posts/', views.posts , name="posts"),
    path('posts/add', views.add_blog , name="add_blog"),
    path('posts/edit/<int:pk>/', views.edit_Post , name="edit_post"),
    path('posts/delete/<int:pk>/', views.delete_post , name="delete_post"),

]
