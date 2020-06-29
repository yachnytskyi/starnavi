import factory


class BaseModelFactory(factory.django.DjangoModelFactory):

    @classmethod
    def _setup_next_sequence(cls):
        k = 1
        try:
            return cls._meta.model.objects.latest('id').id + 1
        except cls._meta.model.DoesNotExist:
            return 1
