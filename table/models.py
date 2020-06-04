from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

table_shape = (
    ('O', 'Oval'),
    ('R', 'Rectangular'),
)


class Table(models.Model):
    number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    hall_name = models.CharField(max_length=200, default='First hall')
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

    def check_size_table(self):
        tables = Table.objects.all()
        check_list = []
        for table in tables:
            check_list.append(range(table.coordinate_x, table.width))
            check_list.append(range(table.coordinate_y, table.height))
        if self.coordinate_x in check_list or self.coordinate_y in check_list:
            return False
        return True




class Reservation(models.Model):
    reservation_date = models.DateField(default=date.today)
    tables = models.ManyToManyField(Table, blank=True)

    class Meta:
        ordering = ['-reservation_date']


