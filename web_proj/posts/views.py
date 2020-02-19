from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
import pdb


def main(request):
    post_list = Post.objects.order_by('-created_at')
    paginator = Paginator(post_list, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'post_list': post_list,
        'posts': posts
    }
    return render(request, 'posts/main.html', context)


def new(request):
    context = {
        'form': PostForm()
    }
    return render(request, 'posts/new.html',  context)


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')


def show(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/show.html', context)


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post,
        'form': PostForm(instance=post)
    }
    return render(request, 'posts/edit.html', context)


def update(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:show', post_id)


def delete(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        post.delete()
        return redirect('main')


def search(request):
    if request.method == "GET":
        post = Post.objects.all()
        search_type = request.GET.get('p', '')
        search_keyword = request.GET.get('keyword', '')
        if search_type == "title":
            if search_keyword:
                post = Post.objects.filter(title__icontains=search_keyword)
        else:
            if search_keyword:
                post = Post.objects.filter(content__icontains=search_keyword)
        context = {
            'posts': post,
            'type': search_type,
            'keyword': search_keyword
        }
        return render(request, 'posts/main.html', context)
