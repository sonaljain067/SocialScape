# Generated by Django 4.2 on 2023-04-12 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_alter_commentpost_post_alter_commentpost_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpost',
            name='post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='social.post'),
        ),
    ]
