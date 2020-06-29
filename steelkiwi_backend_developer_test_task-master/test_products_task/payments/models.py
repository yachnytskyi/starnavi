from __future__ import unicode_literals

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='customer')
    stripe_id = models.CharField(_('Stripe id'), max_length=50, blank=True)

    def __str__(self):
        return '{} {}'.format(self.stripe_id, self.user)


class Order(TimeStampedModel):
    STATUSES = Choices(
        ('succeeded', _('Succeeded')),
        ('pending', _('Pending')),
        ('failed', _('Failed')),
    )

    customer = models.ForeignKey(Customer, related_name='orders')
    amount = models.PositiveIntegerField(_('Amount'))
    status = models.CharField(_('Status'), max_length=15, choices=STATUSES, default=STATUSES.pending)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.id
