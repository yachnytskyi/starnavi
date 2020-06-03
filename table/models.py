from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

table_shape = (
    ('O', 'Oval'),
    ('R', 'Rectangular'),
)


class Table(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    places_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    table_shape = models.CharField(choices=table_shape, default='O', max_length=100)
    coordinate_x = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    coordinate_y = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    width = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    height = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        ordering = ['number']

    def __str__(self):
        return self.number


class Reservation(models.Model):
    reservation_date = models.DateField(auto_now_add=True)
    table = models.ManyToManyField(Table, through='TableReservation')

    class Meta:
        ordering = ['-reservation_date']

    def __str__(self):
        return self.reservation_date


class TableReservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
