from django.db import models
from django.urls import reverse

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Stars(models.Model):
    full_name = models.CharField(max_length=150)
    date_of_birth = models.CharField(max_length=10)
    image = models.ImageField(upload_to="image")
    view = models.IntegerField(default=5)
    
    def __str__(self):
        return self.full_name
    
