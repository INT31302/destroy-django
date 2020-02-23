from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse


def login(request):
    if request.method == "GET":
        context = {
            'form': UserLoginForm()
        }
        return render(request, 'users/login.html', context)
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        user = auth.authenticate(request, user_id=user_id, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
        else:
            context = {
                'form': UserLoginForm(),
                'error': 'username or password is incorrect'
            }
            return render(request, 'users/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('main')


def register(request):
    if request.method == "GET":
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'users/register.html', context)

    if request.method == "POST":
        User = get_user_model()
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
        else:
            context = {
                'form': UserCreationForm()
            }
            return render(request, 'users/register.html', context)
