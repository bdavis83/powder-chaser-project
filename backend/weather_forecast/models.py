from django.db import models
from ski_resort.models import SkiResort

class WeatherForecast (models.Model):
    location = models.ForeignKey(SkiResort, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    high_temp = models.DecimalField(max_digits=5, decimal_places=1)
    low_temp = models.DecimalField(max_digits=5, decimal_places=1)
    wind = models.DecimalField(max_digits=5, decimal_places=1)
    precipitation = models.DecimalField(max_digits=5, decimal_places=1)
    forecast_time = models.DateTimeField(auto_now_add=True)

