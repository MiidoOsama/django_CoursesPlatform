from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    ROLE_CHOICES = (
        ('studens', 'Student'),
        ('teacher', 'Teacher'),
    
    )

    user = models.OneToOneField( User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50 , choices = ROLE_CHOICES , default='student')
    image = models.ImageField(upload_to='profile', blank= True , null= True)

    def __str__(self):
        return self.user.username