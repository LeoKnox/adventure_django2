from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .models import Room, Door

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})

def room_detail(request, room_id):
    try:
        room = Room.objects.get(id=room_id)
    except Room.DoesNotExist:
        raise Http404('Room does not exist. Go Build it!')
    return render(request, 'room_detail.html', {'room': room})

def room_delete(request, room_id):
    Room.objects.get(pk = room_id).delete()
    return redirect('home')

def room_create(request):
    if request.method == "POST":
        new_room = Room()
        new_door = Door()
        new_room.name = request.POST.get('name')
        new_room.description = request.POST.get('description')
        new_room.shape = request.POST.get('shape')
        new_room.width = request.POST.get('width')
        new_room.height = request.POST.get('height')
        new_door = request.POST.get('door')
        new_room.doors.add(request.POST.get(new_door))
        new_room.save()
        new_door = Door(next_room='Guard')
        #new_door.save()
        #new_room.doors.add(new_door)
        return redirect('home')
    doors = Door.objects.all()
    print(doors[0])
    return render(request, 'room_create.html', {'doors': doors})

def room_edit(request, room_id):
    edit_room = Room.objects.get(pk = room_id)
    return render(request, 'room_edit.html', {'edit_room': edit_room})