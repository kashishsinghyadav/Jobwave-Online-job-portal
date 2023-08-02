from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    summary = models.CharField(max_length=100)
    
    education = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    skills = models.CharField(max_length=50)
    
   



# Create your models here.
