from django.urls import path
from . import views

urlpatterns = [
    path('my-courses', views.my_courses , name = 'my_courses'),
    path('lesson/<int:course_id>/', views.lesson_list, name='lesson_list'),
    path('lesson-detail/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
]
