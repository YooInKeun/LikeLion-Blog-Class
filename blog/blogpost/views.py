from django.shortcuts import render, redirect
from .models import Blog

def read_blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs':blogs})

def blog_new(request):
    return render(request, 'blog_new.html')

def create_blog(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.content = request.POST['content']
    blog.save()
    return redirect('read_blog_list')

def read_blog_one(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog' : blog})

def update_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.title = request.POST['title']
    blog.content = request.POST['content']
    blog.save()
    return redirect('read_blog_list')