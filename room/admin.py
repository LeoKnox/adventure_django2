from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'descript', 'floor', 'width', 'length')

admind.site.register(Room, RoomAdmin)