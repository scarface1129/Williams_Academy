from django.shortcuts import render
from .models import *
from courses.models import *
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


def cart(request):
    cart = Cart.objects.get(user_id = request.user)
    Order_ = Order.objects.filter(cart_id = cart.id).order_by('-id')
    course = []
    for order in Order_:
        course_ = Courses.objects.get(id= order.course_id.id)
        course.append(course_)
    price_dollars = [x.Price_dollars for x in course]
    price_dollars = sum(price_dollars)
    price_naira = [x.Price_naira for x in course]
    price_naira = sum(price_naira)
    context = {'course': course, 'price_dollars':price_dollars,'price_naira':price_naira}
    return render(request, 'courses/cart.html', context)


def create_order(request):
    course_id = request.POST.get('course_id')
    user_id = request.POST.get('cart_id')
    Order_ = Order.objects.filter(user_id = request.user)
    already_exsists = False
    for course in Order_:
        if course.course_id.id == int(course_id):
            already_exsists = True
            
    if already_exsists:
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
            instance.user_id = request.user
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
