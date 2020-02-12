from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Product, Brand, Rubric, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm, SearchForm
from django.db.models import Avg
from cart.forms import CartAddProductForm
from haystack.query import SearchQuerySet


def index(request):
	'''домашняя страница магазина'''
	context = {}
	return render(request, 'shop/index.html', context)


def products(request, rubric_slug=None, brand_slug=None):
	'''Отображение всех товаров'''
	products = Product.objects.all()
	title = 'Каталог товаров'
	rubric = None
	brand = None

	if rubric_slug:
		rubric = get_object_or_404(Rubric, slug=rubric_slug)
		products = Product.objects.filter(rubric=rubric)
		title = rubric.name

	if brand_slug:
		brand = get_object_or_404(Brand, slug=brand_slug)
		products = Product.objects.filter(brand=brand)
		title = brand.name

	paginator = Paginator(products, 12)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		products = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		products = paginator.page(paginator.num_pages)
	if 'page' in request.GET:
		page_num = request.GET['page']
	else:
		page_num = 1
	page = paginator.get_page(page_num)
	cart_product_form = CartAddProductForm()
	context = {'products': products, 'title': title, 'current_rubric': rubric,
	'cart_product_form': cart_product_form, 'page': page}
	return render(request, 'shop/products.html', context)

def brand(request):
	context = {}
	return render(request, 'shop/brand.html', context)

# def by_brand(request, brand_slug):
# 	current_brand = get_object_or_404(Brand, slug=brand_slug)
# 	products = Product.objects.filter(brand=current_brand)
# 	title = current_brand.name
# 	context = {'products': products, 'current_brand': current_brand, 'title': title}
# 	return render(request, 'shop/products.html', context)

def product(request, product_slug, brand_slug):
	product = get_object_or_404(Product, slug=product_slug)
	brand_slug = product.brand.slug
	comments = product.comments.filter(is_active=True)
	review_value = Comment.objects.filter(product=product).aggregate(Avg('value'))
	sent = False
	if request.method == 'POST' and 'comment' in request.POST:
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.product = product
			new_comment.save()
			cd = comment_form.cleaned_data
			sent = True
	else:
		comment_form = CommentForm()
	similar_products = Product.objects.filter(rubric=product.rubric).exclude(id=product.id)
	cart_product_form = CartAddProductForm()
	context = {'product': product, 'comments': comments, 'comment_form': comment_form,
	'sent': sent, 'review_value': review_value, 'similar_products': similar_products,
	'cart_product_form': cart_product_form}
	return render(request, 'shop/product.html', context)

def empty(request):
	'''Страница которая находится в разработке'''
	context = {}
	return render(request, 'shop/empty.html', context)

def product_search(request):
	search_form = SearchForm()
	cd = None
	results = None
	total_results = None
	if 'query' in request.GET:
		search_form = SearchForm(request.GET)
		if search_form.is_valid():
			cd = search_form.cleaned_data
			results = SearchQuerySet().models(Product).filter(content=cd['query']).load_all()
			total_results = results.count()
	context = {'search_form': search_form, 'cd': cd, 'results': results, 'total_results': total_results}
	return render(request, 'shop/search.html', context)
