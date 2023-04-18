from rest_framework import serializers
from .models import CurrentWeather

class CurrentWeatherSerializer (serializers.ModelSerializer):
    class Meta:
        model = CurrentWeather
        fields = ['id', 'location', 'condition', 'temperature', 'precipitation', 'wind', 'date_time']
        depth = 1