# Generated by Django 3.2.17 on 2023-07-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csiblog', '0002_postlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='added',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]
