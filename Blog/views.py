from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Post
# Create your views here.


class PostCreate(CreateView):
    template_name = 'blog/create_post.html'
    model = Post
    fields = ['username','text']
    success_url = '/blog'

class PostView(ListView): 
    template_name= 'blog/post_list.html'
    model = Post

class PostUpdate(UpdateView):
    template_name = 'blog/updatepost.html'
    model = Post
    fields = ['username','text']
    success_url = '/blog'

class PostDelete(DeleteView):
    template_name = 'blog/updatepost.html'
    model = Post
    success_url = '/blog'
