from rest_framework import serializers

from test_products_task.products.models import Category, Product, Like, Comment


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.HyperLinkedRelatedField(
        many=True,
        read_only=False,
        view_name='api_detail_product_view'
    )
    product_count = serializers.IntegerField(
        source='products.count',
        read_only=True
    )
    like_count = serializers.IntegerField(
        source='products.likes.count',
        read_only=True
    )

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'products', 'product_count', 'like_count']


class ProductSerializer(serializers.ModelSerializer):
    likes = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False
    )
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = ['id', ' GRADE_CHOICES', 'name', 'slug', 'price', 'image', 'likes', 'comments']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', ' product', 'user', 'ip']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', ' product', 'user', 'ip', 'text', 'pub_date']
