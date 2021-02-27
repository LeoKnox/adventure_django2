from django.urls import include, path
from rest_framework import routers

#from rooms import views
from .views import *

router = routers.DefaultRouter()

router.register(r'apis', RoomsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('dungeon.urls'))
    #path('rooms/', views.room_list),
    #path('rooms/<int:pk>/', views.room_detail),
]