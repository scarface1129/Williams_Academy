from django.shortcuts import render
from courses.models import Courses
import sys
from django.views.generic import DetailView, View, CreateView, UpdateView, ListView
from django.conf import settings
from django.core.mail import send_mail



def home(request):
    courses = Courses.objects.all().order_by('-id')
    print( sys.executable )
    context = {'courses': courses}
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == "POST":
        subject = 'Message from Williams Academy'
        message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )
    return render(request, 'main/contact.html')
