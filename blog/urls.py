from django.urls import  path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('blog-home/', blog_home, name='blog_home'),
    path('blog-single/', blog_single, name='blog_single')
]