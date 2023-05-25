from django import forms
from .models import *

from django.contrib.auth import get_user_model

class CourseCreate(forms.ModelForm):
    class Meta:
        model = Courses 
        fields = [
            
            'Tutor',
            'Image',
            'Name',
            'Rating',
            'Price_dollars',
            'Price_naira',
            'No_of_lessons',
            'Level',
            'Duration',
            'Link',
            
        ]
 

class CourseReview(forms.ModelForm):
    class Meta:
        model = Reviews 
        fields = [
            'course_id',
            'name',
            'email',
            'rating',
            'comment'
        ]