from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie.views import (
    GenreViewSet,
    MovieViewSet,
    NewsViewSet
)

app_name = "movies"

router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'news', NewsViewSet, basename='news')


urlpatterns = [
    path(r'', include(router.urls)),
]