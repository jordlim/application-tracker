from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TrackerSerializer
from .models import Application

# Create your views here.

class TrackerView(viewsets.ModelViewSet):
    serializer_class = TrackerSerializer
    queryset = Application.objects.all()

