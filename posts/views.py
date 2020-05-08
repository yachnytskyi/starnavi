from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from account.models import Account
from posts.models import Post
from posts.serializers import PostSerializer


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_list_post_view(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 10)
    query = request.GET.get('search')
    if query:
        queryset_list = Post.objects.filter(Q(title__icontains=query) |
                                            Q(body__icontains=query))
        serializer = PostSerializer(queryset_list, many=True)
        return Response(serializer.data)
    else:
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        print("2")
        serializer = PostSerializer(page_obj, many=True)
        return Response(serializer.data)


class ApiPostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'body', 'author__username')


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_detail_post_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def api_create_post_view(request):
    account = request.user
    post = Post(author=account)
    if request.method == "POST":
        serializer = PostSerializer(post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def api_update_post_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if post.author != user:
        return Response({'response': "You don't have permissions to edit that."})

    if request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def api_delete_post_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if post.author != user:
        return Response({'response': "You don't have permissions to delete that."})

    if request.method == "DELETE":
        operation = post.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
