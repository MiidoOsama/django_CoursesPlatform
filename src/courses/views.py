from django.shortcuts import render
from .models import Courses , Lesson
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def my_courses(request):
    user = request.user # give me current user who logged in 

    if user.profile.role == 'teacher':
        courses = Courses.objects.filter(teacher = user)
    else:
        courses = Courses.objects.filter(students = user)

    context = {
        'courses': courses
    }
    return render (request , 'courses/course.html', context)