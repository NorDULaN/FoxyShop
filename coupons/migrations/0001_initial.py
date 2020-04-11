# Generated by Django 2.2.10 on 2020-04-09 09:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Значение')),
                ('valid_from', models.DateTimeField(verbose_name='Действительный с')),
                ('valid_to', models.DateTimeField(verbose_name='Действительный до')),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка (%)')),
                ('active', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Купон',
                'verbose_name_plural': 'Купоны',
            },
        ),
    ]