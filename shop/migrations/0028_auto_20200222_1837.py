# Generated by Django 2.2.10 on 2020-02-22 16:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0027_auto_20200220_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='users_like',
        ),
        migrations.AddField(
            model_name='product',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
