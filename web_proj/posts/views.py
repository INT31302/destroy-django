from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.urls import reverse
import pdb
import json
from django.contrib import messages


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
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('main')


def show(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(
        comment=post_id).order_by('-created_date')
    context = {
        'post': post,
        'form': CommentForm(),
        'comments': comments
    }
    return render(request, 'posts/show.html', context)


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.author == request.user:
        context = {
            'post': post,
            'form': PostForm(instance=post)
        }
        return render(request, 'posts/edit.html', context)
    else:
        messages.success(request, '작성자가 아닙니다!')
        return redirect('posts:show', post_id)


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
        if post.author == request.user:
            post.delete()
            return redirect('main')
        else:
            messages.success(request, '작성자가 아닙니다!')
            return redirect('posts:show', post_id)


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


@login_required
@require_POST
def comment(request, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.writer = request.user
            comments.comment = Post.objects.get(pk=post_id)
            comments.save()
            return redirect('posts:show', post_id)


@login_required
def comment_delete(request, post_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.writer == request.user:
        comment.delete()
        return redirect('posts:show', post_id)
    else:
        messages.success(request, '작성자가 아닙니다!')
        return redirect('posts:show', post_id)


@login_required
@require_POST
def like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    post_like, post_like_created = post.like_set.get_or_create(
        user=request.user)

    print(post_like)

    context = {
        'like_count': post.like_count
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


@login_required
@require_POST
def unlike(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    post_unlike, post_unlike_created = post.unlike_set.get_or_create(
        user=request.user)

    print(post_unlike)

    context = {
        'unlike_count': post.unlike_count
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
