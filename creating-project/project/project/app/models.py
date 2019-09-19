from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.CharField(max_length=300)

class Station(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    routes = models.ManyToManyField(Route, related_name='stations')
    name = models.CharField(max_length=300)