from django.db import models
from django.db import models
from django.conf import settings
from courses.models import Courses
from django.urls import reverse
from django.db.models.signals import post_save



# Create your models here.
User = settings.AUTH_USER_MODEL

class Order(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(to=Cart, on_delete=models.CASCADE)

class Cart(models.Model):
    paid = models.BooleanField(default = False)
