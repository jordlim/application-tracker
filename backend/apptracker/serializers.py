from rest_framework import serializers
from .models import AppTracker

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppTracker
        fields = ('id', 'title', 'company', 'applied')