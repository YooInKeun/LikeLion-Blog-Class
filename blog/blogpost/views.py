from django.shortcuts import render
from .models import Blog

def read_blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})