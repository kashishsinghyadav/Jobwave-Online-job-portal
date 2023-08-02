from django.contrib import admin
from apply.models import Apply
class apply_res(admin.ModelAdmin):
    list_display=('apply_icon','apply_info','apply_desc')

admin.site.register(Apply,apply_res)
