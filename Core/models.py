from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    user_types = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin')
    ]
    genders = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique= 1)
    national_id = models.CharField(max_length=14,unique=1)
    address = models.CharField(max_length=300)
    role = models.CharField(max_length=10, choices=user_types)
    gender = models.CharField(max_length=10,choices=genders)
    