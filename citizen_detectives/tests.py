from django.test import TestCase
from .models import Category

# Create your tests here.


class TestCreateCategory(TestCase):
    def test_create_category_title(self):
        title = Category.objects.create(title='Test_Name')
        self.assertEqual(str(title), 'Test_Name')