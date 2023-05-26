from django.db import models
from django.db import models
from django.conf import settings
from courses.models import Courses
from django.urls import reverse
from django.db.models.signals import post_save



# Create your models here.
User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    paid = models.BooleanField(default = True)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user_id.username

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		cart, is_created = Cart.objects.get_or_create(user_id=instance)
		


post_save.connect(post_save_user_receiver, sender=User)


class Order(models.Model):
    course_id = models.ForeignKey(to=Courses, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(to=Cart, on_delete=models.CASCADE)

    def __str__(self):
        return self.cart_id.user_id.Name
    class Meta:
        verbose_name_plural = "Order"