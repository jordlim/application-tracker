from django.contrib import admin
from .models import Application

class TrackerAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'applied')

# Register your models here.

admin.site.register(Application, TrackerAdmin)