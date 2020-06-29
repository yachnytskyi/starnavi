# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from test_products_task.products.views import CategoryListView

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name="home"),
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^products/', include("test_products_task.products.urls", namespace="products")),
    url(r'^users/', include("test_products_task.users.urls", namespace="users")),
    url(r'^payments/', include("test_products_task.payments.urls", namespace="payments")),
]


if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
