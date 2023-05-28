from django.shortcuts import render
from courses.models import Courses
# Create your views here.
from django.views.generic import DetailView, View, CreateView, UpdateView, ListView


def home(request):
    courses = Courses.objects.all().order_by('-id')
    context = {'courses': courses}
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
