from django.test import TestCase


class TestViews(TestCase):

    def test_get_categories_list(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('category_list.html')
    
    def test_get_add_category_page(self):
        response = self.client.get('/add-category/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('add_category.html')
    
    def test_can_add_categories(self):
        response = self.client.post('/add_category/', 
                                    {'title': 'Test Added Category',
                                     'description': 'Test'})
        self.assertRedirects(response, '/categories/')