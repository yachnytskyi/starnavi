from datetime import timedelta
from unittest.case import skipUnless

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from freezegun import freeze_time

from test_products_task.products.models import Category, Product, Like
from test_products_task.products.tests.factories import CategoryFactory, ProductFactory, LikeFactory, CommentFactory
from test_products_task.users.tests.factories import UserFactory

User = get_user_model()


class CategoryListViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = CategoryFactory()
        cls.category_2 = CategoryFactory()
        cls.user = UserFactory()
        cls.url = reverse('products:category_list')

    def create_likes_by_0(self):
        # base products
        self.product_base_20_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.base)
        LikeFactory.create_batch(1, product=self.product_base_20_likes)
        self.product_base_5_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.base)
        LikeFactory.create_batch(1, product=self.product_base_5_likes)
        self.product_base_2_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.base)
        LikeFactory.create_batch(1, product=self.product_base_2_likes)

        # standard
        self.product_standard_20_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.standard)
        LikeFactory.create_batch(1, product=self.product_standard_20_likes)
        self.product_standard_5_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.standard)
        LikeFactory.create_batch(1, product=self.product_standard_5_likes)
        self.product_standard_2_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.standard)
        LikeFactory.create_batch(1, product=self.product_standard_2_likes)

        # premium
        self.product_premium_20_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.premium)
        self.product_premium_5_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.premium)
        self.product_premium_2_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.premium)

    def create_likes_by_1(self):
        # base products
        self.product_base_20_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.base)
        LikeFactory.create_batch(20, product=self.product_base_20_likes)
        self.product_base_5_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.base)
        LikeFactory.create_batch(5, product=self.product_base_5_likes)
        self.product_base_2_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.base)
        LikeFactory.create_batch(2, product=self.product_base_2_likes)

        # standard
        self.product_standard_20_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.standard)
        LikeFactory.create_batch(20, product=self.product_standard_20_likes)
        self.product_standard_5_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.standard)
        LikeFactory.create_batch(5, product=self.product_standard_5_likes)
        self.product_standard_2_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.standard)
        LikeFactory.create_batch(2, product=self.product_standard_2_likes)

        # premium
        self.product_premium_20_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.premium)
        LikeFactory.create_batch(20, product=self.product_premium_20_likes)
        self.product_premium_5_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.premium)
        LikeFactory.create_batch(5, product=self.product_premium_5_likes)
        self.product_premium_2_likes = ProductFactory(category=self.category, grade=Product.GRADE_CHOICES.premium)
        LikeFactory.create_batch(2, product=self.product_premium_2_likes)

    def create_likes_by_3(self):
        # base products
        self.product_base_20_likes = ProductFactory(grade=Product.GRADE_CHOICES.base)
        LikeFactory.create_batch(20, product=self.product_base_20_likes)
        self.product_base_5_likes = ProductFactory(grade=Product.GRADE_CHOICES.base)
        LikeFactory.create_batch(20, product=self.product_base_5_likes)
        self.product_base_2_likes = ProductFactory(grade=Product.GRADE_CHOICES.base)
        LikeFactory.create_batch(10, product=self.product_base_2_likes)

        # standard
        self.product_standard_20_likes = ProductFactory(grade=Product.GRADE_CHOICES.standard)
        LikeFactory.create_batch(20, product=self.product_standard_20_likes)
        self.product_standard_5_likes = ProductFactory(grade=Product.GRADE_CHOICES.standard)
        LikeFactory.create_batch(20, product=self.product_standard_5_likes)
        self.product_standard_2_likes = ProductFactory(grade=Product.GRADE_CHOICES.standard)
        LikeFactory.create_batch(5, product=self.product_standard_2_likes)

        # premium
        self.product_premium_20_likes = ProductFactory(grade=Product.GRADE_CHOICES.premium)
        LikeFactory.create_batch(2, product=self.product_premium_20_likes)
        self.product_premium_5_likes = ProductFactory(grade=Product.GRADE_CHOICES.premium)
        LikeFactory.create_batch(2, product=self.product_premium_5_likes)
        self.product_premium_2_likes = ProductFactory(grade=Product.GRADE_CHOICES.premium)
        LikeFactory.create_batch(2, product=self.product_premium_2_likes)

    @skipUnless(hasattr(Product, 'grade'), 'No need unless grade is added')
    def test_grade_condition_like_empty(self):
        response = self.client.get(self.url)

        grades = Product.GRADE_CHOICES
        grade_list = [
            {'title': grades._display_map[grades.base], 'value': 0},
            {'title': grades._display_map[grades.standard], 'value': 0},
            {'title': grades._display_map[grades.premium], 'value': 0},
        ]
        self.assertEqual(response.context_data['grade_info'], grade_list)

    @skipUnless(hasattr(Product, 'grade'), 'No need unless grade is added')
    def test_grade_condition_like_0(self):
        self.create_likes_by_0()
        response = self.client.get(self.url)

        grades = Product.GRADE_CHOICES
        grade_list = [
            {'title': grades._display_map[grades.base], 'value': 0},
            {'title': grades._display_map[grades.standard], 'value': 0},
            {'title': grades._display_map[grades.premium], 'value': 0},
        ]
        self.assertEqual(response.context_data['grade_info'], grade_list)

    @skipUnless(hasattr(Product, 'grade'), 'No need unless grade is added')
    def test_grade_condition_like_1(self):
        self.create_likes_by_1()
        response = self.client.get(self.url)

        grades = Product.GRADE_CHOICES
        grade_list = [
            {'title': grades._display_map[grades.base], 'value': 1},
            {'title': grades._display_map[grades.standard], 'value': 2},
            {'title': grades._display_map[grades.premium], 'value': 3},
        ]
        self.assertEqual(response.context_data['grade_info'], grade_list)

    @skipUnless(hasattr(Product, 'grade'), 'No need unless grade is added')
    def test_grade_condition_like_3(self):
        self.create_likes_by_3()
        response = self.client.get(self.url)

        grades = Product.GRADE_CHOICES
        grade_list = [
            {'title': grades._display_map[grades.base], 'value': 3},
            {'title': grades._display_map[grades.standard], 'value': 3},
            {'title': grades._display_map[grades.premium], 'value': 3},
        ]
        self.assertEqual(response.context_data['grade_info'], grade_list)

    def test_list(self):
        assert False, 'Not implemented'


class CategoryDetailViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = CategoryFactory()
        cls.product_1 = ProductFactory(category=cls.category, price=30)
        cls.product_2 = ProductFactory(category=cls.category, price=40)
        cls.product_3 = ProductFactory(category=cls.category, price=50)

        cls.user = UserFactory()
        cls.url = reverse('products:category_detail', args=(cls.category.slug, ))

    def test_detail_page(self):
        assert False, 'Not implemented'

    def test_anonymous_filter_price_to(self):
        assert False, 'Not implemented'

    def test_anonymous_filter_price_from(self):
        assert False, 'Not implemented'

    def test_anonymous_filter_price_from_and_to(self):
        assert False, 'Not implemented'

    def test_anonymous_filter_following_empty(self):
        assert False, 'Not implemented'

    def test_anonymous_filter_following(self):
        assert False, 'Not implemented'

    def test_user_detail_page(self):
        assert False, 'Not implemented'

    def test_user_filter_following_by_like(self):
        assert False, 'Not implemented'

    def test_user_filter_following_by_comment(self):
        assert False, 'Not implemented'

    def test_user_filter_following_by_like_and_comment(self):
        assert False, 'Not implemented'


class LikeToggleTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = CategoryFactory()
        cls.product_1 = ProductFactory(category=cls.category, price=30)

        cls.user = UserFactory()
        cls.url_like = reverse('products:like_toggle', args=(cls.product_1.id, ))

    def test_invalid_product(self):
        assert False, 'Not implemented'
    
    def test_anonymous_like_product(self):
        assert False, 'Not implemented'

    def test_anonymous_dislike_product(self):
        assert False, 'Not implemented'

    def test_user_like_product(self):
        assert False, 'Not implemented'

    def test_user_dislike_product(self):
        assert False, 'Not implemented'
