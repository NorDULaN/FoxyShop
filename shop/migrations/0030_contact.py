# Generated by Django 2.2.10 on 2020-03-04 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20200222_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True, verbose_name='имя')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('body', models.TextField(max_length=300, verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='contacts/', verbose_name='скриншот')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['created'],
            },
        ),
    ]