from django.db import models

# Create your models here.

class SensorValues(models.Model):
    date = models.DateTimeField(auto_now=True)
    raining = models.BooleanField(default=False, blank=True)
    temperature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    # ...
