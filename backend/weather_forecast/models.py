from django.db import models
from ski_resort.models import SkiResort

class WeatherForecast (models.Model):
    location = models.ForeignKey(SkiResort, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    high_temp = models.CharField(max_length=255)
    low_temp = models.CharField(max_length=255)
    wind = models.CharField(max_length=255)
    precipitation = models.CharField(max_length=255)
    forecast_time = models.TimeField()
    
