from django.contrib.auth.models import AbstractUser
from django.db import models


# ------------------------
# 1. USER MODELI
# ------------------------
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='media/user/', null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"