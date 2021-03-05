from django.db import models

class Room(models.Model):
    MONSTERS = [('Orc', 'Orc'), ('Skeleton', 'Skeleton'), ('Dragon', 'Dragon')]
    name = models.CharField(max_length = 50)
    description = models.TextField()
    monster = models.CharField(max_length = 100, choices=MONSTERS)
    width = models.IntegerField()
    heigh = models.IntegerField()
    doors = models.ManyToManyField('Door')

class Door(models.Model):
    next_room = models.CharField(max_length=50)