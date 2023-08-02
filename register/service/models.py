from django.db import models

class Service(models.Model):
    testi_icon=models.CharField(max_length=50)
    testi_name=models.CharField(max_length=50)
    testi_sub_name=models.CharField(max_length=80)
    testi_desc=models.CharField(max_length=80)
    testi_follow=models.TextField()

# Create your models here.
