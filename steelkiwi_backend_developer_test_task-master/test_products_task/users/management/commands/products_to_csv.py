import csv
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.models import Count
from django.db.models.expressions import F

from products.models import Product

User = get_user_model()


class Command(BaseCommand):
    help = "Get products and users who set more than 1 comment per day"
    fields = ['id', 'name', 'comment_count', 'like_count']

    def add_arguments(self, parser):
        parser.add_argument('-comment', type=int,  nargs='?', default=0)
        parser.add_argument('-like', type=int, nargs='?', default=0)
        parser.add_argument('-path', type=str, nargs='?', default='products.csv')

    def handle(self, *args, **options):
        comment_count = options['comment']
        like_count = options['like']
        # TODO use path from argument
        # path = options['path']
        path = '/products.csv'

        queryset = Product.objects.annotate(
            like_count=Count(F('likes')),
            comment_count=Count(F('comments'))
        ).filter(
            like_count__gte=like_count,
            comment_count__gte=comment_count,
        ).values(*self.fields)

        dirname = os.path.dirname(__file__)
        full_path = dirname + path
        with open(full_path, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.fields)
            for element in queryset:
                writer.writerow([element[field_name] for field_name in self.fields])
        self.stdout.write('Generation has been finished.')
