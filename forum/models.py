from django.db import models

class Articles(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, verbose_name = 'Название')
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Статью'
        verbose_name_plural='Статьи'


class Comment(models.Model):
    post = models.ForeignKey(Articles, related_name='comments', on_delete = models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)