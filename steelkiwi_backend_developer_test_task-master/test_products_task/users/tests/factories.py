import string
import uuid

import factory
from django.conf import settings
from faker import Faker

from test_products_task.common.factories import BaseModelFactory

User = settings.AUTH_USER_MODEL
TEST_USER_PASSWORD = uuid.uuid4().hex
fake = Faker()


class UserFactory(BaseModelFactory):
    username = factory.Sequence(lambda n: 'username_{}'.format(n))
    email = factory.Sequence(lambda n: 'email{}@email.com'.format(n))
    password = factory.PostGenerationMethodCall('set_password', TEST_USER_PASSWORD)
    first_name = factory.Sequence(lambda n: 'first {}'.format(n))
    last_name = factory.Sequence(lambda n: 'last {}'.format(n))

    class Meta:
        model = User
