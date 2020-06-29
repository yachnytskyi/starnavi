import datetime
from collections import OrderedDict
from datetime import timedelta

from braces.views import JSONResponseMixin, AjaxResponseMixin
from django.contrib import messages
from django.db.models import Sum, Case, When, IntegerField, Count, F, Q
from django.db.models.functions import Coalesce
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, FormView, TemplateView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view

from test_products_task.common.mixins import ActiveTabMixin
from test_products_task.common.utils import get_ip_from_request
from test_products_task.products.forms import LikeForm
from test_products_task.products.models import Category, Product, Like, Comment
from test_products_task.products.serializers import CategorySerializer, ProductSerializer, LikeSerializer, \
    CommentSerializer


@api_view(['GET', 'POST'])
def api_list_category_view(request):
    if request.method == 'GET':
        category_list = Category.objects.all()
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        category_create = Category()
        serializer = CategorySerializer(category_create, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail_category_view(request, slug):
    try:
        category_detail = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category_detail)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CategorySerializer(category_detail, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        operation = category_detail.delete()
        data = {}

        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


@api_view(['GET', 'POST'])
def api_list_product_view(request):
    if request.method == 'GET':
        product_list = Product.objects.all()
        serializer = ProductSerializer(product_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        product_create = Product()
        serializer = ProductSerializer(product_create, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def api_detail_product_view(request, slug):
    try:
        product_detail = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product_detail)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = ProductSerializer(product_detail, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        operation = product_detail.delete()
        data = {}

        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


@api_view(['GET', 'POST'])
def api_list_like_view(request, slug):
    if request.method == 'GET':
        like_list = Like.objects.all()
        serializer = LikeSerializer(like_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        like_create = Like()
        like_create.product = Product.objects.get(slug=slug)
        if like_create.product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LikeSerializer(like_create, data=request.data)
        if serializer.is_valid():
            if like_create.user is not None:
                like_create.ip = None
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def api_detail_like_view(request, like_id):
    try:
        like_detail = Like.objects.get(id=like_id)
    except Like.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = like_detail.delete()
        data = {}

        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


@api_view(['GET', 'POST'])
def api_list_comment_view(request, slug):
    if request.method == 'GET':
        comment_list = Comment.objects.filter(pub_date__range=(timezone.now(), timezone.now() - timedelta(days=1)))
        serializer = CommentSerializer(comment_list, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        comment_create = Comment()
        comment_create.product = Product.objects.get(slug=slug)
        if comment_create.product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(comment_create, data=request.data)
        if serializer.is_valid():
            if comment_create.user is not None:
                comment_create.ip = None
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def api_detail_comment_view(request, comment_id):
    try:
        comment_detail = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment_detail)
        return Response(serializer.data)

    if request.method == 'DELETE':
        operation = comment_detail.delete()
        data = {}

        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)


class AddToCartView(AjaxResponseMixin, JSONResponseMixin, FormView):
    http_method_names = ('post',)
    success_url = reverse_lazy('products:cart')

    def post(self, request, *args, **kwargs):
        raise NotImplementedError


class CartView(ActiveTabMixin, TemplateView):
    active_tab = 'cart'
    template_name = 'products/cart.html'
