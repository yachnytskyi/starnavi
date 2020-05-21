from rest_framework import serializers

from payments.models import Status, Payment


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'number', 'amount', 'aim', 'status', 'date_published']


class StatusesSerializer(serializers.ModelSerializer):
    payment_set = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='number'
    )

    class Meta:
        model = Status
        fields = ['id', 'type', 'payment_set']
