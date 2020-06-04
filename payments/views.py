from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payments.models import Status, Payment
from payments.serializers import StatusesSerializer, PaymentsSerializer


@api_view(['GET', ])
def api_list_status_view(request):
    status_list = Status.objects.all()
    serializer = StatusesSerializer(status_list, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def api_detail_status_view(request, status_id):
    try:
        status_detail = Status.objects.get(pk=status_id)
    except Status.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StatusesSerializer(status_detail)
    return Response(serializer.data)


@api_view(['POST', ])
def api_create_status_view(request):
    status_create = Status()
    serializer = StatusesSerializer(status_create, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def api_update_status_view(request, status_id):
    try:
        status_update = Status.objects.get(pk=status_id)
    except Status.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StatusesSerializer(status_update, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "update successful"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_status_view(request, status_id):
    try:
        status_delete = Status.objects.get(pk=status_id)
    except Status.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    operation = status_delete.delete()
    data = {}

    if operation:
        data["success"] = "delete successful"
    else:
        data["failure"] = "delete failed"
    return Response(data=data)


@api_view(['GET', ])
def api_list_payment_view(request):
    payment_list = Payment.objects.all()
    serializer = PaymentsSerializer(payment_list, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def api_detail_payment_view(request, payment_id):
    try:
        payment_detail = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PaymentsSerializer(payment_detail)
    return Response(serializer.data)


@api_view(['POST', ])
def api_create_payment_view(request):
    try:
        payment_create = Payment()
        serializer = PaymentsSerializer(payment_create, data=request.data)
        data = {}
    except Payment.status.DoesNotExist:
        data["failure"] = "This foreign key doesn't exist"
        return data

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
def api_update_payment_view(request, payment_id):
    try:
        payment_update = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist or Payment.status.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PaymentsSerializer(payment_update, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "update successful"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def api_delete_payment_view(request, payment_id):
    try:
        payment_delete = Payment.objects.get(pk=payment_id)
    except Payment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    operation = payment_delete.delete()
    data = {}

    if operation:
        data["success"] = "delete successful"
    else:
        data["failure"] = "delete failed"
    return Response(data=data)
