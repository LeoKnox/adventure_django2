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
    print("Door id")
    print(door_id)
    room_id = request.POST.get('room_id')
    Door.objects.get(pk = door_id).delete()
    return redirect('home')

def edit_delete(request, door_id, room_id):
    Door.objects.get(pk = door_id).delete()
    return redirect('room_edit', room_id)

def room_delete(request, room_id):
    Room.objects.get(pk = room_id).delete()
    return redirect('home')

def door_edit(request):
    add_door = Door(next_room = request.POST.get('new_door'))
    add_door.save()
    room_id = request.POST.get('room_id')
    return redirect('room_edit', room_id)

def door_add(request):
    #print('door added' + str(request.POST.get('new_door')))
    add_door = Door(next_room = request.POST.get('new_door'))
    add_door.save()
    return redirect('room_create')

def room_create(request):
    if request.method == "POST":
        new_room.name = request.POST.get('name')
        new_room.description = request.POST.get('description')
        new_room.shape = request.POST.get('shape')
        new_room.width = request.POST.get('width')
        new_room.height = request.POST.get('height')
        new_room.save()
        new_door = request.POST.getlist('doors')
        for nd in new_door:
            single_door = Door(next_room = nd)
            single_door.save()
            new_room.doors.add(single_door)
        return redirect('home')
    doors = Door.objects.all()
    rooms = Room.objects.all()
    room_shapes = Room.SHAPES
    return render(request, 'room_create.html', {'doors': doors, 'rooms':rooms, 'room_shapes':room_shapes})

def room_edit(request, room_id):
    edit_room = Room.objects.get(pk = room_id)
    shapes = Room.SHAPES
    doors = Room.objects.all()
    doors = [val for val in edit_room.doors.values_list('next_room', flat=True) if val not in Room.objects.values_list('name', val)] # delete if other door_dupe later
    #for dupe in door_dupe:
        #print(Door.objects.get(next_room = dupe.door))
    print('***** !!!!!!! *****')
    print(doors)
    #door_dupe = [val for val in Room.objects.values_list('name', flat=True) if val not in edit_room.doors.values_list('next_room', flat=True)]
    door_dupe = edit_room.doors.values_list('next_room', flat=True)
    #door_dupe.values_list('next_room', flat=True)
    #door_dupe = Room.objects.exclude(name__in = edit_room.doors)
    if request.method == "POST":
        if request.POST.get('name') != "":
            edit_room.name = request.POST.get('name')
        if request.POST.get('description') != "":
            edit_room.description = request.POST.get('description')
        print(request.POST.get('description') == "")
        if request.POST.get('shape') != "":
            edit_room.shape = request.POST.get('shape')
        if request.POST.get('width') != "":
            edit_room.width = request.POST.get('width')
        if request.POST.get('height') != "":
            edit_room.height = request.POST.get('height')
        edit_room.save()
        new_door = request.POST.getlist('doors') #doesn't but does now!
        for nd in new_door:
            #single_door = Door.objects.get(room = nd)
            single_door = Door(next_room = nd)
            print(single_door.next_room)
            edit_room.doors.add(single_door)
        return redirect('home')
    return render(request, 'room_edit.html', {'edit_room': edit_room, 'doors':doors, 'door_dupe':door_dupe})

def edit_door(request, door_id=121):
    edit_door = Door.objects.get(id = door_id)
    if request.method == "POST":
        print(request.POST.get('next_room'))
        if request.POST.get('next_room') != "":
            edit_door.next_room = request.POST.get('next_room')
        edit_door.save()
        return redirect('home')
    return render(request, 'edit_door.html', {'edit_door': edit_door})

def dd_test(request):
    if request.method == "POST":
        #request.POST.get('room_add')
        #new_door = request.POST.getlist('room_add')
        print(request.POST.getlist('room_add'))
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')