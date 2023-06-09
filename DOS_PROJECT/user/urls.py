from django.urls import path
# from . import views
from .views import *


urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
    path('logout/', logout_view, name='logout'),
    path('registerd_course/', Registered_Courses.as_view(), name='registered_course'),
    path('registerd_course_detail/<pk>', RegisteredCourseDetail.as_view(), name='registered-course-detail'),
    path('module/<pk>', ModuleDetail.as_view(), name='module'),
]