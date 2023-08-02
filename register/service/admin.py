from django.contrib import admin

from service.models import Service

class service_admin(admin.ModelAdmin):
    list_display=('testi_icon','testi_name','testi_sub_name','testi_desc','testi_follow')
admin.site.register(Service,service_admin)

# Register your models here.
