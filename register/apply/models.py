from django.db import models
from tinymce.models import HTMLField

class Apply(models.Model):
    apply_icon=models.CharField(max_length=80)
    apply_info=models.CharField(max_length=80)
    apply_desc=HTMLField()

# Create your models here.
