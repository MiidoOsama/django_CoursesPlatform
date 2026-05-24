from django.shortcuts import render
from .models import Courses , Lesson
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
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


@login_required
def lesson_list(request, course_id):
    course = get_object_or_404(Courses, id = course_id)
    user = request.user # give me current user who logged in 

    if user.profile.role == 'teacher':
        if course.teacher != user:
            return HttpResponseForbidden()

    else:
        if user not in course.students.all():
            return HttpResponseForbidden()

    lessons = course.lessons.all()

    context = {
        'lessons': lessons,
        'course': course,
    }

    return render(request, 'courses/lesson_list.html', context)


@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    course = lesson.course
    user = request.user

    if user.profile.role == 'teacher':
        if course.teacher != user:
            return HttpResponseForbidden()
    else:
        if user not in course.students.all():
            return HttpResponseForbidden()

    context = {
        'lesson': lesson,
        'course': course,
    }

    return render(request, 'courses/course_details.html', context)


    
