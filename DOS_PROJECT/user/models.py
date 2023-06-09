from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from courses.models import Courses



User = settings.AUTH_USER_MODEL

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Registered_Course(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(to=Courses, on_delete=models.CASCADE, related_name='my_course') 
    
    def __str__(self):
        return f'{self.user_id.username}({self.course_id.Name})'