from django.db import models
from django.db import models
from django.conf import settings
from courses.models import Courses
from django.urls import reverse
from django.db.models.signals import post_save
import JSONField
# from django.contrib.postgres.fields import JSONField


# Create your models here.
User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # course_id = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    orders = JSONField(default=dict)