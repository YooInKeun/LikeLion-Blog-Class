from django.urls import path
from django.views.generic import RedirectView
import blogpost.views

urlpatterns = [
    path('list', blogpost.views.read_blog_list, name='read_blog_list'),
    path('new', blogpost.views.blog_new, name='blog_new'),
    path('create', blogpost.views.create_blog, name='create_blog'),
    path('detail/<int:pk>', blogpost.views.read_blog_one, name="read_blog_one"),
    path('update/<int:pk>', blogpost.views.update_blog, name="update_blog"),
]
