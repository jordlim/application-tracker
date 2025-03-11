# filepath: /Users/jflim/Desktop/repos/application-tracker/backend/apptracker/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'applications', views.TrackerView, basename='applications')

urlpatterns = [
    path('', include(router.urls)),
]