from rest_framework import serializers
from .models import Application

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'title', 'company', 'applied')