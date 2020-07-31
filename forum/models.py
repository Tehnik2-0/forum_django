from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    creation_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, verbose_name = 'Название')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank = True, 
        null = True
    )
    body = models.TextField()
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'

class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete = models.CASCADE, verbose_name='Статья', blank=True, null=True, related_name='comments_articles')
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор коментария', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now=True)
    body = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)