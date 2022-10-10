from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm


def index(request):
    return render(request, 'snpapp/index.html', {'title': 'index'})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'snpapp/register.html', {'form': form,'title':'Register'})


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' Welcome {username} !')
            return redirect('index')
        else:
            messages.info(request, f'Account does not exist')
    form = AuthenticationForm()
    return render(request, 'snpapp/login.html', {'form':form,'title':'Log in'})

