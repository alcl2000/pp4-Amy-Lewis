from django.test import TestCase


class TestViews(TestCase):

    def test_get_categories_list(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('category_list.html')