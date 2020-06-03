from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

# from account.models import Account
from posts.models import Post
from posts.serializers import PostSerializer


@api_view(['GET', ])
def api_list_post_view(request):
    post_list = Post.objects.all()
    page_number = request.GET.get('page')
    query = request.GET.get('search')
    ordering = request.GET.get('ordering')
    filtration = request.GET.get('filtration')
    filter_type = request.GET.get('filter_type')
    start_date = request.GET.get('start_date', '2020-1-1')
    end_date = request.GET.get('end_date', '2040-1-1')
    filters = {}
    if start_date != '2020-1-1' or end_date != '2020-1-1':
        post_list = post_list.filter(date_published__range=(start_date, end_date))

    if filter_type == 'icontains' or filter_type is None:
        filters = {
            'body': 'body__icontains',
            'title': 'title__icontains',
            'author': 'author__username__icontains',
        }
    if filter_type == 'startswith':
        filters = {
            'body': 'body__startswith',
            'title': 'title__startswith',
            'author': 'author__username__startswith',
        }
    query_filters = None

    if filtration == 'or' or filtration is None:
        for key, value in filters.items():
            if key in request.GET:
                if query_filters is None:
                    query_filters = Q(**{value: request.GET[key]})
                else:
                    query_filters = query_filters | Q(**{value: request.GET[key]})
    if filtration == 'and':
        for key, value in filters.items():
            if key in request.GET:
                post_list = post_list.filter(**{value: request.GET[key]})
    if query_filters is not None:
        post_list = post_list.filter(query_filters)

    if query:
        post_list = post_list.filter(Q(title__icontains=query) |
                                     Q(body__icontains=query) |
                                     Q(author__username__icontains=query))
    if ordering:
        post_list = post_list.order_by(ordering)

    paginator = Paginator(post_list, 10)
    page_obj = paginator.get_page(page_number)
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
def api_detail_post_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post)
    return Response(serializer.data)


@api_view(['POST', ])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_create_post_view(request):
    account = request.user
    post = Post(author=account)
    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_update_post_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if post.author != user:
        return Response({'response': "You don't have permissions to edit that."})

    serializer = PostSerializer(post, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "update successful"
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def api_delete_post_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if post.author != user:
        return Response({'response': "You don't have permissions to delete that."})

    operation = post.delete()
    data = {}
    if operation:
        data["success"] = "delete successful"
    else:
        data["failure"] = "delete failed"
    return Response(data=data)
