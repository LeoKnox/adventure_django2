from django.shortcuts import render
from django.views.decoratots.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rooom.models import Room
from rooms.serializers import RoomSerializer

@csrt_exempt
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return JsonResponse(serializer.data, safe=Fale)
    
    elif request.method = 'POST':
        data = JSONParser().parse(request)
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, satus=201)
        return JsonResponse(serializer.errors, status=400)