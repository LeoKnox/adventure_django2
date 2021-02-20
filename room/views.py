from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import RoomSerializer
from .models import Room

def home(request):
    context = {'form': PostForm()}
    return render(request, 'room/templates/index.html', context)

@api_view(['GET'])
def room_collection(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def room_element(request, pk):
    try:
        room = Room.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = RoomSerializer(post)
        return Response(serializer.data)

'''
class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
'''