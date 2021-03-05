from django.db import models

class Room(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    monster = models.CharField(max_length = 100)
    width = models.IntegerField()
    heigh = models.IntegerField()