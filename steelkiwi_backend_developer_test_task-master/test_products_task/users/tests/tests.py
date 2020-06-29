from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from test_products_task.products.tests.factories import LikeFactory, CommentFactory
from test_products_task.users.tests.factories import UserFactory

User = get_user_model()

