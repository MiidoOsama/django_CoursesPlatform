from django.urls import path
from . import views
urlpatterns = [
    path('login', views.user_login , name = 'login'),
    path('logout', views.user_logout , name = 'logout'),
    path('register', views.user_registeration , name = 'register'),

]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    

