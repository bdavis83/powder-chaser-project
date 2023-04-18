from django.db import models
from ski_resort.models import SkiResort

class HistoricalWeather (models.Model):
    location = models.ForeignKey(SkiResort, on_delete=models.CASCADE)
    date = models.DateField()
    high_temp = models.CharField(max_length=255)
    low_temp = models.CharField(max_length=255)
    precipitation = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)

