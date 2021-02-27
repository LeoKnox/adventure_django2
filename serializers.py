from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.Serializer):
    class Meta:
        model = Room
        fields = ('name', 'description', 'width', 'length')
    '''
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)
    width = serializers.IntegerField()
    length = serializers.IntegerField()
    '''

def create(self, validated_data):
    return Room.ojbects.create(**validated_data)

def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.description = validated_data.get('description', instance.description)
    instance.width = validated_data.get('width', instance.width)
    instance.length = validated_data.get('length', instance.length)
    instance.save()
    return instance