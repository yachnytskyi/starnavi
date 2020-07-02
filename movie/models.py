from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=100)


class Movie(models.Model):
    year = models.IntegerField()
    country = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    compositor = models.CharField(max_length=200)
    screenwriter = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    operator = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre, blank=True, null=True)
    budget = models.CharField(max_length=200)
    adult = models.IntegerField()
    time = models.CharField(max_length=100)


class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    movie = models.ManyToManyField(Movie, blank=True, null=True)

