from django.contrib import admin
from django.urls import path

from rooms import views

app_name = 'rooms'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('rooms/edit/<int:room_id>/', views.room_edit, name='room_edit'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('rooms/create/', views.room_create, name='room_create'),
    path('rooms/delete/<int:room_id>', views.room_delete, name='room_delete'),
    path('rooms/door_delete/<int:door_id>', views.door_delete, name='door_delete'),
    path('rooms/door_edit/<int: door_id>', views.door_edit, name='door_edit'),
    path('room/door_add/', views.door_add, name="door_add"),
]
