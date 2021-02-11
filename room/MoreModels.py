from django.db import models

class MyDungeon(models.Model):
    dungeon_id = models.IntField(blank=False, primary_key=True)
    dungeon_name = models.CharField(max_length=20)