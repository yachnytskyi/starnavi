from django.urls import path
from table.views import (
    api_list_table_view,
    api_detail_table_view,
    api_list_reservation_view,
    api_detail_reservation_view,
)

app_name = "tables"

urlpatterns = [
    path('', api_list_table_view, name="list"),
    path('<int:table_id>/', api_detail_table_view, name="detail"),
    path('reservations/', api_list_reservation_view, name="list"),
    path('reservations/<int:reservation_id>/', api_detail_reservation_view, name="detail"),
]
