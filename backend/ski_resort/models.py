from django.db import models

class SkiResort (models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=4)
    longitude = models.DecimalField(max_digits=4)
    favorite = models.ForeignKey()