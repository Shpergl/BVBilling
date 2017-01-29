from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from models import Post, Comments
from post.forms import CommentsForm
from post.models import Post, Comments


def home(request):
    posts = Post.objects.all()
    context = {
        "posts" : posts
    }
    return render(request, 'post/home.html', context)

def posts_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'post/home.html', context)

def about(request):
    return render(request, 'post/about.html')

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comments.objects.filter(post = id)
    context = {
    "post" : post,
    "comments" : comments,
    "form" : CommentsForm,
    }
    context.update(csrf(request))

    return render(request, 'post/post.html', context)

def add_like(request, id):
    post = get_object_or_404(Post, id=id)
    post.likes +=1
    post.save()
    return redirect('post-detail', id=id)

def add_comment(request, id):
    form = CommentsForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        post = get_object_or_404(Post, id=id)
        comment = Comments(text = text, post=post)
        comment.save()
        return redirect ('post-detail', id=id)
    else:
        return redirect('about')


