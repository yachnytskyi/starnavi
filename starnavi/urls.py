"""starnavi URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from posts.views import (
    api_detail_post_view,
    api_create_post_view,
    api_update_post_view,
    api_delete_post_view,
    )
app_name = 'posts'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('posts/<int:post_id>/', api_detail_post_view, name="detail"),
    path('posts/<int:post_id>/update/', api_update_post_view, name="update"),
    path('posts/create/', api_create_post_view, name="create"),
    path('posts/<int:post_id>/delete/', api_delete_post_view, name="delete"),

]

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
#
# ]