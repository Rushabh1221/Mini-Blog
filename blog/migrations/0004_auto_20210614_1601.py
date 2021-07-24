# Generated by Django 3.0.7 on 2021-06-14 10:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.BigIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
