from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Post
        fields = ['title', 'body', 'date_published', 'date_updated', 'post_like', 'post_unlike', 'username']

    def get_username_from_author(self, post):
        username = post.author.username
        return username
