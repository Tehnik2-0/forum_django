from django.test import TestCase
from forum.models import Article
from django.urls import reverse


class TestClassArticle(TestCase):
    def test_article(self):
        article = Article.objects.create(title='Test article 1', body='Test text article 1')
        self.assertEqual(article.__str__(), 'Test article 1')