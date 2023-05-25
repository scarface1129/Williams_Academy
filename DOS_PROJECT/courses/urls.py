from django.urls import path
from .views import *

app_name = 'courses'
urlpatterns = [
    path('update/<slug>/', UpdateCourses.as_view(), name=('course_update')),
    path('create/', CreateCourses.as_view(), name=('course_create')),
    # path('review/', CreateReviews.as_view(), name=('course_reviews')),
    path('review/', create_review, name=('course_reviews')),
    path('', courses, name='courses'),
    path('course_detail/<pk>', CourseDetail.as_view(), name='course_detail'),
]