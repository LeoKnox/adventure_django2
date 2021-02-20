from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import RoomSerializer
from .models import Room

def home(request):
    context = {'form': PostForm()}
    return render(request, 'room/templates/index.html', context)

@api_view(['GET'], 'POST')
def room_collection(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'name': request.DATA.get('the_room'), 'description': request.description.pk}
        serializer = RoomSerlializer(data=data)
        if serializer.isvalid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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