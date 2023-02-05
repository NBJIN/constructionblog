# Generated by Django 3.2.17 on 2023-02-05 22:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('csiblog', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no_of_likes',
            field=models.ManyToManyField(related_name='csiblog_no_of_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]