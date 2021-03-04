from rest_framework import ListAPIView

from rooms.serializers import RoomSerializer
from rooms.models import Room

class RoomList(LIstAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer