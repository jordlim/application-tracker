from django.contrib import admin
from .models import AppTracker

class TrackerAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'applied')

# Register your models here.

admin.site.register(AppTracker, TrackerAdmin)