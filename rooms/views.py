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

def door_delete(request, door_id):
    Door.objects.get(pk = door_id).delete()
    return redirect('home')

def room_delete(request, room_id):
    Room.objects.get(pk = room_id).delete()
    return redirect('home')

def door_edit(request, door_id):
    return redirect('room_edit', door_id)

def room_create(request):
    if request.method == "POST":
        '''
        new_room = Room()
        new_door = Door()
        new_room.name = request.POST.get('name')
        new_room.description = request.POST.get('description')
        new_room.shape = request.POST.get('shape')
        new_room.width = request.POST.get('width')
        new_room.height = request.POST.get('height')
        new_door = request.POST.getlist('doors')
        new_room.doors.add(request.POST.get(new_door))
        new_room.save()
        print("new door = " + new_door)
        new_door = Door(next_room='Entry')
        new_door = Door(next_room = request.POST.get(new_door))
        new_room.doors.add(new_door)
        new_door.save()
        '''
        print('doors ' + request.POST.get('new_door'))
        return redirect('home')
    doors = Door.objects.all()
    return render(request, 'room_create.html', {'doors': doors})

def room_edit(request, room_id):
    edit_room = Room.objects.get(pk = room_id)
    shapes = Room.SHAPES
    #print (shapes[1][0]) #use to populate room shape forms
    doors = Door.objects.all()
    if request.method == "POST":
        next_room = request.POST.getlist('doors') #doesn't but does now!
        #next_room = request.POST.get('name') #works
        print(next_room)
        return redirect('home')
    return render(request, 'room_edit.html', {'edit_room': edit_room, 'doors':doors})