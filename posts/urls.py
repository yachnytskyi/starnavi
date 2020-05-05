from django.urls import path
from posts.views import (
    api_detail_post_view,
    api_create_post_view,
    api_update_post_view,
    api_delete_post_view,
    ApiPostListView,
    api_list_post_view
)

app_name = "posts"

urlpatterns = [
    # path('', ApiPostListView.as_view(), name="list"),
    path('', api_list_post_view, name="list"),
    path('<int:post_id>/', api_detail_post_view, name="detail"),
    path('<int:post_id>/update/', api_update_post_view, name="update"),
    path('create/', api_create_post_view, name="create"),
    path('<int:post_id>/delete/', api_delete_post_view, name="delete"),
]
