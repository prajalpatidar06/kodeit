from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('about', views.about , name='about'),
    path('register', views.user_register , name='register'),
    path('_login', views.user_login, name='_login'),
    path('logout', views.user_logout, name='logut'),
    path('post_blog', views.post_blog, name='post_blog'),
    path('blog_detail/<int:id>', views.blog_detail, name='blog_detail'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('search', views.search, name='search'),
]
