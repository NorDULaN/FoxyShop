# Generated by Django 2.2.10 on 2020-03-11 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='text',
        ),
    ]
