from django.db import models

class Room(models.Model):
    SHAPES = [('Square', 'Square'), ('Circle', 'Circle'), ('Oval', 'Oval')]
    name = models.CharField(max_length = 50)
    description = models.TextField()
    shape = models.CharField(max_length = 100, choices=SHAPES)
    width = models.IntegerField()
    heigh = models.IntegerField()
    doors = models.ManyToManyField('Door')

class Door(models.Model):
    next_room = models.CharField(max_length=50)

    def __str__(self):
        return self.next_room