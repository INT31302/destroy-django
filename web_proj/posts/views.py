from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
import pdb


def main(request):
    return render(request, 'posts/main.html')


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
