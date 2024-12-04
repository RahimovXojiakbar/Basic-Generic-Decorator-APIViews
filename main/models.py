from django.db import models

class WeatherModel(models.Model):
    city = models.CharField(max_length=200)
    temp = models.IntegerField()
    description = models.TextField()
    wind_speed  = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.city
