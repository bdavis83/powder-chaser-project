from rest_framework import serializers
from .models import WeatherForecast

class WeatherForecastSerializer (serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        fields = ['id', 'location', 'condition','high_temp', 'low_temp', 'wind', 'precipitation', 'forecast_time', 'user_id']
        depth = 1