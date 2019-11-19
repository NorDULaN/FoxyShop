from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Product

def index(request):
	'''домашняя страница магазина'''
	return render(request, 'shop/index.html')


def products(request):
	'''Отображение всех товаров'''
	products = Product.objects.all()
	context = {'products': products}
	return render(request, 'shop/products.html', context)