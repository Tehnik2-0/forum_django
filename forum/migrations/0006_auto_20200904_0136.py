# Generated by Django 3.0.8 on 2020-09-03 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Видимость статьи'),
        ),
    ]
