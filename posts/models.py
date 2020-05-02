from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=True)
    body = models.TextField(max_length=5000, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='date published')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='date updated')
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_like = models.IntegerField(default=0, verbose_name='post like')
    post_unlike = models.IntegerField(default=0, verbose_name='post unlike')

    def __str__(self):
        return self.title
