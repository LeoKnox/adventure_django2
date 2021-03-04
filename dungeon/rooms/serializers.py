from rest_framework import serializers
from rooms.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'length', 'width')
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['is_empty'] = instance.is_empty()
        data['random_encounter'] = instance.random_encounter()
        return data