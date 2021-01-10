from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=32)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=1000)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Event_member(models.Model):
    user_id = models.IntegerField()
    event_id = models.IntegerField()

    def __str__(self):
        return str(self.pk)