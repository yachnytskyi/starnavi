from rest_framework import serializers

from movie.models import Genre, Movie, News


class GenreSerializer(serializers.ModelSerializer):
    movie_set = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)

    class Meta:
        model = Genre
        fields = ("id", "title", "movie_set")


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=False)

    class Meta:
        model = Movie
        fields = ("id", "year", "genre", "country", "producer",
                  "compositor", "screenwriter",
                  "producer", "operator", "genre", "budget", "adult", "time")


class NewsSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True, read_only=False)

    class Meta:
        model = News
        fields = ("id", "title", "body", "movie")
