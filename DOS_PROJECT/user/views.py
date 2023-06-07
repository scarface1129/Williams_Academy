from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import UserLogin, UserSignUp 
from allauth.socialaccount.models import SocialAccount
from django.http import HttpResponseRedirect


# Create your views here.

def login_user(request):
    form = UserLogin()
    next = ""

    if request.GET:  
        next = request.GET['next']
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            print('next',next)
            if next == "":
                return redirect('home')
            else:
                return HttpResponseRedirect(next)
                
                
                    

    context = {
        'form': form,
        'next': next
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