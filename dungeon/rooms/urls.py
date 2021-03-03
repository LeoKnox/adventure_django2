from django.urls import path
from snippets import views

urlpatterns = [
    path('rooms/', views.room_list),
    path('rooms/<int:pk>/', views.rooms_detail)
]