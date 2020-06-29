# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include
from test_products_task.payments import views

urlpatterns = [
    url(r'^order/pay/$', views.OrderPayView.as_view(), name='order_pay'),
    url(r'^orders/$', views.OrderListView.as_view(), name='order_list'),
    url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetailView.as_view(), name='order_detail'),
]
