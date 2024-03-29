from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'floor', 'width', 'length')

admin.site.register(Room, RoomAdmin)