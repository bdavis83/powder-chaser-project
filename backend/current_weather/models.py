from django.db import models

class CurrentWeather(models.Model):
    location = models.ForeignKey(SkiResort, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    precipitation = models.CharField(max_length=255)
    wind = models.CharField(max_length=255)
    date_time = models.DateTimeField()

