from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    dungeo = serializers.SlurRelatedField(
        queryset=Dungeon.objects.all(), slug_field='dungeonname'
    )
    class Meta:
        model = Room
        fields = ('id', 'name', 'description', 'floor', 'width', 'length')