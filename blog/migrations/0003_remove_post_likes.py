# Generated by Django 3.0.7 on 2021-05-21 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
