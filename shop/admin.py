from django.contrib import admin
from .models import Product, Brand, Rubric, Comment, Contact

class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'availability', 'date_added', 'slug', 'brand', 'rubric')
	list_display_links = ('title', 'availability')
	search_fields = ('title', 'availability', 'date_added', 'brand', 'rubric')
	list_editable = ['brand', 'rubric']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Product, ProductAdmin)

class BrandAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Brand, BrandAdmin)

class RubricAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Rubric, RubricAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'product', 'created', 'is_active']
	search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)

class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'created', 'body']

admin.site.register(Contact, ContactAdmin)
