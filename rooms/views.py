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

def room_create(request):
    if request.method == "POST":
        
        #new_room = Room.objects.create(name = 'Tower', description='Tall room', shape='Square', width=7, height=7)
        new_room = Room()
        new_room.name = request.POST.get('name')
        print (new_room.name)
        new_door = Door(next_room='Guard')
        #new_door.save()
        #new_room.doors.add(new_door)
        return redirect('home')
    return render(request, 'room_create.html')

def room_edit(request, room_id):
    return render(request, 'room_edit.html')