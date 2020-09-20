from django.test import TestCase
from forum.models import Article


class TestHomeListView(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title='Test article 1',
            body='Test text article 1'
        )

    def test_base_page(self):
        response = self.client.get('http://your_server_ip:8000')
        title = response.context['object_list'].get().__str__()
        self.assertEqual(
            title,
            self.article.title
        )


class TestDetailView(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title='Test article 1',
            body='Test text article 1'
        )

    def test_detail_page(self):
        self.client.post(
            '/register',
            {'username': 'admin',
             'password': '123456'}
        )
        self.client.post(
            '/login',
            {'username': 'admin',
             'password': '123456'}
        )
        response = self.client.get('/detail/4')
        title = response.context['get_article']
        self.assertEqual(
            title.__str__(),
            self.article.title
        )


class TestArticleCreateView(TestCase):
    def test_create_page(self):
        self.client.post(
            '/register',
            {'username': 'admin',
             'password': '123456'}
        )
        self.client.post(
            '/login',
            {'username': 'admin',
             'password': '123456'}
        )
        response = self.client.get('/edit-page')
        self.assertEqual(
            response.status_code,
            200
        )


class TestArticleUpdateView(TestCase):
    def test_update_page(self):
        self.client.post(
            '/register',
            {'username': 'admin',
             'password': '123456'}
        )
        self.client.post(
            '/login',
            {'username': 'admin',
             'password': '123456'}
        )
        post = {
            'title': 'article 2',
            'body': 'body article 2'
        }
        self.client.post(
            '/edit-page',
            post
        )
        response = self.client.get('/update-page/3')
        self.assertEqual(
            response.status_code,
            200
        )


class TestForumLogoutView(TestCase):
    def test_logout(self):
        self.client.post(
            '/register',
            {'username': 'admin',
             'password': '123456'}
        )
        self.client.post(
            '/login',
            {'username': 'admin',
             'password': '123456'}
        )
        response = self.client.get('/')
        user = response.context['user'].__str__()
        self.assertEqual(
            user,
            'admin'
        )
        self.client.get('/logout')
        response = self.client.get('/')
        user = response.context['user'].__str__()
        self.assertEqual(
            user,
            'AnonymousUser'
        )


class TestArticleDeleteView(TestCase):
    def test_delete_page(self):
        self.client.post(
            '/register',
            {'username': 'admin',
             'password': '123456'}
        )
        self.client.post(
            '/login',
            {'username': 'admin',
             'password': '123456'}
        )
        post = {
            'title': 'article 3',
            'body': 'body article 3'
        }
        self.client.post(
            '/edit-page',
            post
        )
        self.client.post('/delete-page/2')
        response = self.client.get('/detail/2')
        self.assertEqual(
            response.status_code,
            404
        )
