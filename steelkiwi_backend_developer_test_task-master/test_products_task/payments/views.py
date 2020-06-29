import json

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from test_products_task.payments.forms import OrderPayForm
from test_products_task.payments.models import Order, Customer


class OrderPayView(FormView):
    template_name = 'payments/order_pay.html'
    form_class = OrderPayForm
    success_url = reverse_lazy('payments:order_list')

    @method_decorator([login_required, ])
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class OrderListView(ListView):
    model = Order
    template_name = 'payments/order_list.html'
    @method_decorator([login_required, ])
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



class OrderDetailView(DetailView):
    model = Order
    template_name = 'payments/order_detail.html'
    @method_decorator([login_required, ])
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
