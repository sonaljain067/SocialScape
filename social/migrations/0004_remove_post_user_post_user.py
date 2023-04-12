# Generated by Django 4.2 on 2023-04-11 09:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0003_alter_post_comments_count_alter_post_likes_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ManyToManyField(related_name='posts_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
