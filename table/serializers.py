from rest_framework import serializers

from table.models import Table, Reservation



class ReservationSerializer(serializers.ModelSerializer):
    tables_set = serializers.SlugRelatedField(
        # queryset=Table.objects.all(),
        many=True,
        read_only=True,
        slug_field='number',
    )

    class Meta:
        model = Reservation
        fields = ('id', 'reservation_date', 'tables_set')


class TableSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Table
        fields = ('id', 'number', 'hall_name', 'places_amount', 'table_shape',
                  'coordinate_x', 'coordinate_y', 'width', 'height', 'reservations')



