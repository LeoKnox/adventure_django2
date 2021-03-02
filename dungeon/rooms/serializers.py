from rest_framework import serializers
from rooms.models import Room

class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length = 50)
    description = serializers.CharField()
    width = Serializers.IntegerField()
    height = Serializers.IntegerField()

    def create(self, validated_data):
        return Room.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.width = validated_data.get('width', instance.width)
        instance.height = validated_data.get('height', instance.height)
        instance.save()
        return instance