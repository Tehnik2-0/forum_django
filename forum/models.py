from django.db import models

class Articles(models.Model):
    creation_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, verbose_name = 'Название')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'

