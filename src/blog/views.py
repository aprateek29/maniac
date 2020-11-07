from django.shortcuts import render
from .models import Post

def index(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, 'blog/index.html', context)

def single_post(request):
    return render(request, 'blog/post.html', {})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    post_list = Post.objects.all()
    context = {
        'post': post,
        'post_list': post_list
    }
    return render(request, 'blog/post-detail.html', context)

def about(request):
    return render(request, 'blog/about.html', {})

def contact(request):
    return render(request, 'blog/contact.html', {})