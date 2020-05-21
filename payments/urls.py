from django.urls import path
from payments.views import (
    api_list_status_view,
    api_detail_status_view,
    api_create_status_view,
    api_update_status_view,
    api_delete_status_view,
    api_list_payment_view,
    api_detail_payment_view,
    api_create_payment_view,
    api_update_payment_view,
    api_delete_payment_view,
)

app_name = "payments"

urlpatterns = [
    path('status/', api_list_status_view, name="list"),
    path('status/<int:status_id>/', api_detail_status_view, name="detail"),
    path('status/create/', api_create_status_view, name="create"),
    path('status/<int:status_id>/update/', api_update_status_view, name="update"),
    path('status/<int:status_id>/delete/', api_delete_status_view, name="delete"),
    path('', api_list_payment_view, name="list"),
    path('payment/<int:payment_id>/', api_detail_payment_view, name="detail"),
    path('payment/create/', api_create_payment_view, name="create"),
    path('payment/<int:payment_id>/update/', api_update_payment_view, name="update"),
    path('payment/<int:payment_id>/delete/', api_delete_payment_view, name="delete"),
]
