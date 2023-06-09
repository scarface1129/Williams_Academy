from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import UserLogin, UserSignUp 
from allauth.socialaccount.models import SocialAccount
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, View, CreateView, UpdateView, ListView
from .models import Registered_Course
from courses.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


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



class Registered_Courses(LoginRequiredMixin, ListView):
    login_url = "/user/login/"
    template_name = 'user/registered_course.html'
    def get_queryset(self):
        return Registered_Course.objects.filter(user_id=self.request.user)


class RegisteredCourseDetail(LoginRequiredMixin, DetailView):
    login_url = "/user/login/"
    template_name = 'user/registered_course_detail.html'
    def get(self,request,*args, **kwargs):
        id_ = self.kwargs['pk']
        RegisteredCourse = Registered_Course.objects.get(id=id_)
        course = Courses.objects.get(id = RegisteredCourse.course_id.id)
        curriculum = Curriculum.objects.get(course=course)
        module = Module.objects.filter(curriculum=curriculum)
        context = {'course':course,'module':module}     
        return render(request, 'user/registered_course_detail.html',context)
    
class ModuleDetail(LoginRequiredMixin,DetailView):
    login_url = "/user/login/"
    def get(self,request,*args, **kwargs):
        id_ = self.kwargs['pk']
        module = Module.objects.get(id=id_)
        context = {'module':module}     
        return render(request, 'user/module.html',context)