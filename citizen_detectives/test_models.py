from django.test import TestCase
from citizen_detectives.models import Category

# Create your tests here.

if __name__ == '__main__':
    unittest.main()


class TestCreateCategory(TestCase):

    def test_create_category_title(self):
        title = Category.objects.create(title='Test Name')
        self.assertEqual(str(title), 'Test Name')
        r = Category.objects.create(slug='test-name')
        self.assertEqual(r, "Test-Name")

    def test_create_category_description(self):
        self.assertEqual(category_desc(description), 'Test Description')