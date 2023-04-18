from django.db import models
from ski_resort.models import SkiResort

class CurrentWeather(models.Model):
    location = models.ForeignKey(SkiResort, on_delete=models.CASCADE)
    condition = models.DecimalField(max_digits=5, decimal_places=1)
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    precipitation = models.DecimalField(max_digits=5, decimal_places=1)
    wind = models.DecimalField(max_digits=5, decimal_places=1)
    date_time = models.DateTimeField(auto_now_add=True)

