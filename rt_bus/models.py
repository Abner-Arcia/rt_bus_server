from django.db import models
from datetime import datetime

class Bus(models.Model):
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    capacity = models.PositiveSmallIntegerField()
    route = models.ForeignKey('Route', on_delete=models.DO_NOTHING)
    lat = models.FloatField()
    lng = models.FloatField()
    creation_date = models.DateTimeField(default=datetime.now())

class Route(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    points = models.JSONField()