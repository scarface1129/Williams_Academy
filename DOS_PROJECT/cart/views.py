from django.shortcuts import render
from .models import *
from django.views.generic import DetailView, View, CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.core import serializers
from django.shortcuts import render,get_object_or_404, redirect
from .forms import *    
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse


# class CreateOrder(LoginRequiredMixin,CreateView):
#     form_class = OrderForm
#     login_url = '/login/'

#     def form_valid(self, form):               
#         obj = form.save(commit=False)
#         return super(CreateOrder, self).form_valid(form)
    
    
def create_order(request):
    course_id = request.POST.get('course_id')
    user_id = request.POST.get('cart_id')
    cart_id = Cart.objects.get(user_id = user_id)
    if Order.objects.filter(course_id = course_id) and Order.objects.filter(cart_id = cart_id):
        ser_instance = serializers.serialize('json', [])
        return JsonResponse({"instance": ser_instance}, status=200)
        # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        form = OrderForm(request.POST)
        # save the data and after fetch the object in instance
        id = request.POST.get('cart_id')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.cart_id = Cart.objects.get(user_id = id)
            order = Order.objects.filter(cart_id = instance.cart_id.id)
            instance.save()
            ser_instance = len(order)
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
