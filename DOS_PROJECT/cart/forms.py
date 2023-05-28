from django import forms
from .models import *

from django.contrib.auth import get_user_model



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = [
            'cart_id',
            'course_id',
            
        ]