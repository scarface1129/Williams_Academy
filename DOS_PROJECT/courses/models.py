from django.db import models
from django.conf import settings
from django.urls import reverse

class Courses(models.Model):
    Tutor = models.CharField(max_length = 100)
    Image       = models.FileField(upload_to='media',blank=False, null=False)
    Name = models.CharField(max_length = 100)
    Rating = models.IntegerField()
    Price_dollars = models.IntegerField()
    Price_naira = models.IntegerField()
    No_of_lessons = models.IntegerField()
    Duration = models.IntegerField()
    Level = models.CharField(max_length = 100, default = 'BEGINNER')
    Link = models.CharField(max_length = 200)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)
    course_description = models.TextField(max_length=3000, null=True)
    
    
    
    def __str__(self):
        return self.Name
    def get_absolute_url(self):
        return reverse("courses")
    class Meta:
        verbose_name_plural = "courses"
        
        
class Curriculum(models.Model):
    course = models.OneToOneField(to = Courses, on_delete = models.CASCADE)
    detail = models.TextField(max_length=1000)
    def __str__(self):
        return self.course.Name
    # def get_absolute_url(self):
    #     return reverse("courses")
    class Meta:
        verbose_name_plural = "Curriculums"
        
class Module(models.Model):
    curriculum = models.ForeignKey(to=Curriculum, on_delete = models.CASCADE)
    module_number = models.IntegerField()
    module_name = models.CharField(max_length=50)
    video             = models.FileField(upload_to= 'media',blank=True, null=True)
    module_content       = models.TextField(blank=True, null=True, help_text="separate each content by a comma")
    
    def __str__(self):
        return f"{self.curriculum.course.Name} (module {self.module_number})"
    def get_content(self):
        return self.module_content.split(',')
    
class Reviews(models.Model):
    course_id = models.ForeignKey(to = Courses, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateField(auto_now=True)
    rating = models.IntegerField()
    comment = models.TextField(max_length=2000)
   
    
    def __str__(self):
        return self.course_id.Name
    
    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs= {'pk':self.course_id.id})
    
    class Meta:
        verbose_name_plural = "Review"
        ordering=[ '-created_at' ]