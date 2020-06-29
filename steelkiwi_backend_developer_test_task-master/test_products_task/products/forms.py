from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from config import settings
from test_products_task.products.models import Like, Product

User = get_user_model()


class LikeForm(forms.Form):
    user = forms.ModelChoiceField(User.objects.all(), required=False)
    product = forms.ModelChoiceField(Product.objects.all())
    ip = forms.GenericIPAddressField(required=False)


