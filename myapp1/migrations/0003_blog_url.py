# Generated by Django 3.2.4 on 2021-06-05 10:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_remove_blog_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.URLField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
