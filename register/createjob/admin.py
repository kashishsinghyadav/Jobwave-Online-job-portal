from django.contrib import admin
from createjob.models import Create

class Show(admin.ModelAdmin):
    list_display=('create_info','create_desc','create_link')

admin.site.register(Create,Show)

# Register your models here.
