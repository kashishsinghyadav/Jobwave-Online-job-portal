from django.contrib import admin
from resumedata.models import Resume

class res(admin.ModelAdmin):
    list_display = ('name','address', 'city','state','phone' ,'email','summary','education','experience','skills')

# Register your models here.
admin.site.register(Resume,res)