from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=100) 
    teacher = models.ForeignKey(User,on_delete=models.CASCADE , related_name = 'teachers')
    students = models.ManyToManyField(User, related_name = 'enrolled_students', blank= True)
    image = models.ImageField(upload_to='courses',blank = True , null= True)
    def __str__(self):
        return self.name 






class Lesson(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.title