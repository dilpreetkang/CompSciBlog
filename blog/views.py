from django.shortcuts import render
from blog.models import Blog
from blog.models import Todo
from blog.models import About

def blog_index(request):
    blogs = Blog.objects.all()
    todos = Todo.objects.all()
    abouts = About.objects.all()
    context = {
        'blogs' : blogs,
        'todos' : todos,
        'abouts' : abouts
        }
    return render(request, 'blog_index.html',context)

def blog_detail(request, pk) :
    blog = Blog.objects.get(pk=pk)
    context = {
        'blog' : blog
        }
    return render(request, 'blog_detail.html',context)

def todo_index(request,pk):
    todo =Todo.objects.get (pk=pk)
    context = {
        'todo' : todo
        }
    return render (request, 'todo_index.html', context)

def about_index(request):
    abouts = About.objects.all()
    context = {
        'abouts' : abouts
         }
    return render (request, 'about_index.html', context)
    