from django.shortcuts import render, redirect
from .models import *

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

    json = {"Mon" : [1, 0, 1, 1, 1], "Tues" : [1, 0, 0, 1, 1]}
    time_table = TimeTable2()
    time_table.the_json = json
    time_table.save()
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

def delete_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    return redirect('read_blog_list')