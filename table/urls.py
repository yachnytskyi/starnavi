from django.urls import path
from table.views import (
    api_list_reservation_view
)

app_name = "tables"

urlpatterns = [
    # path('', ApiPostListView.as_view(), name="list"),
    path('', api_list_reservation_view, name="list"),
    # path('<int:post_id>/', api_detail_post_view, name="detail"),
    # path('<int:post_id>/update/', api_update_post_view, name="update"),
    # path('create/', api_create_post_view, name="create"),
    # path('<int:post_id>/delete/', api_delete_post_view, name="delete"),
]
