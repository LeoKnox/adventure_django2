from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    floor = models.CharField(max_length=50)
    width = models.IntegerField()
    length = models.IntegerField()

    def _str_(self):
        return self.name