# Generated by Django 3.2.17 on 2023-02-05 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csiblog', '0006_post_no_of_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]