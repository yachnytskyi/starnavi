# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from test_products_task.products import views

urlpatterns = [
    url(r'^$', views.api_list_category_view, name='category_list'),
    url(r'^(?P<products>)$', views.api_list_product_view),
    url(r'^(?P<comments>)$', views.api_list_comment_view),
    url(r'^cart/$', views.CartView.as_view(), name='cart'),
    url(r'^(?P<product_slug>.+)/like/$', views.api_detail_like_view, name='like_toggle'),
    url(r'^(?P<product_slug>.+)/add/to/cart/$', views.AddToCartView.as_view(), name='add_to_cart'),
    url(r'^(?P<category_slug>.+)/(?P<product_slug>.+)/$', views.api_detail_product_view, name='product_detail'),
    url(r'^(?P<category_slug>.+)/$', views.api_detail_category_view, name='category_detail'),
]
