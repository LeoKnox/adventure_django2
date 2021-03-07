from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>New Rooms</p>')

def room_detail(request, room_id):
    return HttpResponse(f'<p>Room number {room_id}</p>')