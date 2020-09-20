from django.test import TestCase
from forum.models import Article, Comment


class TestClassArticle(TestCase):
    def setUp(self):
        self.article = Article.objects.create(title='Test article 1', body='Test text article 1')

    def test_article(self):
        self.assertEqual(self.article.title, 'Test article 1')
        self.assertEqual(self.article.body, 'Test text article 1')


class TestClassComment(TestCase):
    def setUp(self):
        self.comment = Comment.objects.create(body='Test text comment 1')

    def test_comment(self):
        self.assertEqual(self.comment.body, 'Test text comment 1')
