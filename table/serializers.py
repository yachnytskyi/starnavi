from rest_framework import serializers

from table.models import Table, Reservation


class ReservationSerializer(serializers.ModelSerializer):
    # tables = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='number',
    # )
    tables = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all(),
        many=True,
    )

    class Meta:
        model = Reservation
        fields = ('id', 'reservation_date', 'tables')


class TableSerializer(serializers.ModelSerializer):
    reservation_set = ReservationSerializer(many=True, read_only=False)

    class Meta:
        model = Table
        fields = ('id', 'number', 'hall_name', 'places_amount', 'table_shape',
                  'coordinate_x', 'coordinate_y', 'width', 'height', 'reservation_set')
