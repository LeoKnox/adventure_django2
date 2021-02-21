from django.db import models

class Room(models):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    width = models.IntegerField()
    length = models.IntegerField()