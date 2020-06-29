from django.contrib import admin

from test_products_task.payments.models import Customer, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class ChargeAdmin(admin.ModelAdmin):
    pass
