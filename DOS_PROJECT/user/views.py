from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import UserLogin, UserSignUp 
from allauth.socialaccount.models import SocialAccount

# Create your views here.

def login_user(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_teacher:
                    login(request, user)
                    return redirect('home')
                if user.is_student:
                    login(request, user)
                    return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)

def register_user(request):
    form = UserSignUp()
    if request.method == "POST":
        form = UserSignUp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')