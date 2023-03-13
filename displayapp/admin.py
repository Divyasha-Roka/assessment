from django.contrib import admin
from .models import Display
# Register your models here.
class DisplayAdmin(admin.ModelAdmin):
    list_display = ['id', 'name' , 'price' , 'image']

admin.site.register(Display , DisplayAdmin)