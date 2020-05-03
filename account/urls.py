from django.urls import path
from account.views import (
    registration_view,
)

app_name = "account"

urlpatterns = [
    path('register/', registration_view, name="register"),
]
