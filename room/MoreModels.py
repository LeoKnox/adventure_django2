from django.db import models

class MyDungeon(models.Model):
    dungeon_name = models.CharField(max_length=20)

    class Meta:
        order = ['-dungeon_name']

        def get_abs_url(self):
            return reve('model-detail-view', args=[str(self.id)])
        
        def __str__(self):
            return self.dungeon_name