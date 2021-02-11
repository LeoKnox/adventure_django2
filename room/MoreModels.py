from django.db import models

class MyDungeon(models.Model):
    dungeon_id = models.IntegerField(blank=False, primary_key=True)
    dungeon_name = models.CharField(max_length=20)

class MyRoom(models.Model):
    room_id = models.IntegerField(blank=False, primary_key=True)
    room_name = models.CharField(max_length=20)
    width = models.IntegerField()
    length = models.IntegerField()