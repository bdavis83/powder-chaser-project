from rest_framework import serializers
from .models import HistoricalWeather

class HistoricalWeatherSerializer (serializers.ModelSerializer):
    class Meta:
        model = HistoricalWeather
        fields = ['id', 'location', 'date', 'high_temp', 'low_temp', 'precipitation', 'condition']
        depth = 1