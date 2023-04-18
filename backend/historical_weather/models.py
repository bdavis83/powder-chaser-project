from django.db import models
from ski_resort.models import SkiResort

class HistoricalWeather (models.Model):
    location = models.ForeignKey(SkiResort, on_delete=models.CASCADE)
    date = models.DateField()
    high_temp = models.DecimalField(max_digits=5, decimal_places=1)
    low_temp = models.DecimalField(max_digits=5, decimal_places=1)
    precipitation = models.DecimalField(max_digits=5, decimal_places=1))
    condition = models.CharField(max_length=255)

