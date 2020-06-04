from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from table.models import Table, Reservation
from table.serializers import TableSerializer, ReservationSerializer


@api_view(['GET', 'POST'])
def api_list_reservation_view(request):
    if request.method == 'GET':
        reservation_list = Reservation.objects.all()
        serializer = ReservationSerializer(reservation_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        reservation_create = Reservation()
        serializer = ReservationSerializer(reservation_create, data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = f"Hello, you ordered the {request.POST.get('tables')} table on" \
                      f"this time {request.POST.get('reservation_date')}"
            send_mail('Review',
                      message,
                      settings.EMAIL_HOST_USER,
                      [request.POST.get('user.email')],
                      fail_silently=False
                      )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail_reservation_view(request, reservation_id):
    try:
        reservation_detail = Reservation.objects.get(pk=reservation_id)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservationSerializer(reservation_detail)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ReservationSerializer(reservation_detail, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        operation = reservation_detail.delete()
        data = {}

        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


@api_view(['GET', 'POST'])
def api_list_table_view(request):
    if request.method == 'GET':
        table_list = Table.objects.all()
        serializer = TableSerializer(table_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        table_create = Table()
        serializer_check = True
        tables = Table.objects.all()
        check_list = []
        for table in tables:
            check_list += list(range(table.coordinate_x, table.coordinate_x + table.width + 1))
            check_list += list(range(table.coordinate_y, table.coordinate_y + table.width + 1))
        print(check_list)

        if int(request.POST.get('coordinate_x')) in check_list or int(request.POST.get('coordinate_y')) in check_list:
            data = {}
            serializer_check = False
            data["failure"] = "These coordinates are busy, you can't use them"
            return Response(data=data)
        if int(request.POST.get('coordinate_x')) + int(request.POST.get('width')) > 100 \
                or int(request.POST.get('coordinate_y')) + int(request.POST.get('width')) > 100:
            data = {}
            serializer_check = False
            data["failure"] = "You can place a table only in our hall!"
            return Response(data=data)

        serializer = TableSerializer(table_create, data=request.data)
        if serializer.is_valid():
            if serializer_check:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail_table_view(request, table_id):
    try:
        table_detail = Table.objects.get(pk=table_id)
    except Table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TableSerializer(table_detail)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TableSerializer(table_detail, data=request.data)
        serializer_check = True
        tables = Table.objects.all()
        check_list = []
        for table in tables:
            check_list += list(range(table.coordinate_x, table.coordinate_x + table.width + 1))
            check_list += list(range(table.coordinate_y, table.coordinate_y + table.width + 1))
        print(check_list)

        if int(request.POST.get('coordinate_x')) in check_list or int(request.POST.get('coordinate_y')) in check_list:
            data = {}
            serializer_check = False
            data["failure"] = "These coordinates are busy, you can't use them"
            return Response(data=data)
        if int(request.POST.get('coordinate_x')) + int(request.POST.get('width')) > 100 \
                or int(request.POST.get('coordinate_y')) + int(request.POST.get('width')) > 100:
            data = {}
            serializer_check = False
            data["failure"] = "You can place a table only in our hall!"
            return Response(data=data)
        data = {}
        if serializer.is_valid():
            if serializer_check:
                serializer.save()
                data["success"] = "update successful"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        operation = table_detail.delete()
        data = {}

        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
