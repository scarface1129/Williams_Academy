from django.shortcuts import render
from django.views.generic import DetailView, View, CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from user.models import *
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.shortcuts import render,get_object_or_404, redirect
from .forms import *    
# from users.utils import code_generator
from django.http import HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


class CreateCourses(LoginRequiredMixin,CreateView):
    template_name = 'courses/create_course.html'
    form_class = CourseCreate
    login_url = '/login/'

    def form_valid(self, form):               
        obj = form.save(commit=False)
        return super(CreateCourses, self).form_valid(form)

class UpdateCourses(LoginRequiredMixin,UpdateView):
    template_name = 'courses/update_course.html'
    form_class = CourseCreate
    login_url = '/login/'

    def get_context_data(self,*args, **kwargs):
        context = super(UpdateCourses, self).get_context_data(*args, **kwargs)
        slug = self.kwargs['slug']
        course = Courses.objects.filter(id = slug)
        context['course'] = course
        return context
    
    def get_queryset(self):
        slug = self.kwargs['slug']
        return Courses.objects.filter(id = slug)
    
@login_required(login_url='/user/login/')
def courses(request):
    reg_courses = Registered_Course.objects.filter(user_id=request.user.id)
    courses = Courses.objects.exclude(my_course__in=reg_courses).order_by('-id')
    context = {'courses': courses}
    return render(request, 'courses/courses.html', context)



class CourseDetail(LoginRequiredMixin,DetailView):
    login_url = "/user/login/"
    # redirect_field_name = 'redirect_to'
    def get(self,request,*args, **kwargs):
        course_id = self.kwargs['pk']
        course = Courses.objects.get(id=course_id)
        courses = Courses.objects.all()
        curriculum = Curriculum.objects.get(course=course.id)
        module = Module.objects.filter(curriculum=curriculum.id)
        reviews = Reviews.objects.filter(course_id=course.id)
        rating = Reviews.objects.filter(course_id=course.id)[:3]
        print(rating)
        rating_count = [x.rating for x in reviews]
        rating_len = len(reviews)
        if rating_len > 0 : 
            rating_count = round(sum(rating_count)/rating_len)
        else:
            rating_count =  0
        context = {
            'object':course,
            'courses':courses, 
            'curriculum':curriculum,
            'module':module, 
            'Reviews':rating, 
            'rating_count':rating_count,
            'rating_len':rating_len,
            'range':range(rating_count),
            }     
        return render(request, 'courses/course_details.html',context)
    
# class CreateReviews(LoginRequiredMixin,CreateView):
#     form_class = CourseReview
#     # login_url = 'course'
#     def form_valid(self, form):               
#         obj = form.save(commit=False)
#         return super(CreateReviews, self).form_valid(form)
    
def create_review(request):
    # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        form = CourseReview(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occured
    return JsonResponse({"error": ""}, status=400)
