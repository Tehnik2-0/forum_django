from django.test import TestCase
from forum.models import Article


class TestHomeListView(TestCase):
    def test_base_page(self):
        article = Article.objects.create(title='Test article 1', body='Test text article 1')
        response = self.client.get('http://your_server_ip:8000')
        title = response.context['object_list'].get().__str__()
        self.assertEqual(title, 'Test article 1')


class TestDetailView(TestCase):
    def test_detail_page(self):
        article = Article.objects.create(title='Test article 1', body='Test text article 1')
        response = self.client.get('http://your_server_ip:8000')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/register', {'username': 'admin', 'password': '123456'})
        response = self.client.post('/login', {'username': 'admin', 'password': '123456'})
        response = self.client.get('/')
        user = response.context['user']
        user = user.__str__()
        self.assertEqual(user, 'admin')
        article = Article.objects.create(title='Test article 1', body='Test text article 1')
        response = self.client.get('/detail/2')
        title = response.context['get_article']
        self.assertEqual(title.__str__(), 'Test article 1')



