from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from table.models import Table, Reservation
from table.serializers import TableSerializer, ReservationSerializer

@api_view(['GET', ])
def api_list_reservation_view(request):
    reservation_list = Reservation.objects.all()
    serializer = ReservationSerializer(reservation_list, many=True)
    return Response(serializer.data)