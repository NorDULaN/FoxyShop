import os
from django.db import models

# def get_image_path(instance, filename):
# 	return os.path.join('photos', str(instance.id), filename)

class Product(models.Model):
	"""Товар публикуемый на сайте"""
	# image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	title = models.CharField(max_length=50, verbose_name='Название')
	text = models.TextField(max_length=400, verbose_name='Характеристики')
	price = models.IntegerField(verbose_name='Цена')
	availability = models.BooleanField(default=True, verbose_name='Наличие')
	date_added = models.DateTimeField(auto_now_add=True, verbose_name='Был добавлен')
	brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Производитель')

	class Meta:
		verbose_name_plural = 'Товар' 
		verbose_name = 'Товар'
		ordering = ['price']

class Brand(models.Model):
	"""Производитель"""
	name = models.CharField(max_length=20, primary_key=True, db_index=True, verbose_name='Название')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Производители'
		verbose_name = 'Производитель'
		ordering = ['name']