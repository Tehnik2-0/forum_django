from django.db import models
from django.contrib.auth.models import User
from .middleware import get_current_user
from django.db.models import Q


class Article(models.Model):
    creation_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class StatusFilterComment(models.Manager):
    def get_queryset(self):
        if get_current_user() == 'None':
            return super().get_queryset().filter(
                Q(status=False, author=get_current_user()) |
                Q(status=False, article__author=get_current_user()) |
                Q(status=True)
            )
        else:
            return super().get_queryset().filter(Q(status=True))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='comments_articles', verbose_name='Статья'
                                )
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор коментария', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now=True)
    body = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость статьи', default=True)
    objects = StatusFilterComment()

    class Meta:
        ordering = ['-id']
