from django.db import models

class Create(models.Model):
    create_info=models.CharField(max_length=50)
    create_desc=models.CharField(max_length=80)
    create_link=models.TextField()




# Create your models here.
