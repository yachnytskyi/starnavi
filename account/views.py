from rest_framework import status
from rest_framework.status import HTTP_404_NOT_FOUND

from account.models import Account
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from account.serializers import RegistrationSerializer, AccountPropertiesSerializer
from rest_framework.authtoken.models import Token


@api_view(['GET', ])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def account_properties_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = AccountPropertiesSerializer(account)
    return Response(serializer.data)


@api_view(['PUT', ])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def update_account_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    serializer = AccountPropertiesSerializer(account, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['response'] = 'Account updated success'
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user."
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)
