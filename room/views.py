from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RoomSerializer
from .models import Room

class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()