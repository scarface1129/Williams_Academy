from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about_us/', about, name='about'),
    path('contact_us/', contact, name='contact'),
]