# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices


@python_2_unicode_compatible
class User(AbstractUser):
    ACTIVITY_PARAM = 'activity'
    ACTIVITY_OPTIONS = Choices(
        ('no_like', _('No like')),
        ('no_comment', _('No comment')),
        ('no_like_and_no_comment', _('No like and comment')),
    )

    def __str__(self):
        return self.username
