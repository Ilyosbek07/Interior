from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from products.models import CaruselModel, ProductModel, CallModel


class MyTranslationAdmin1(TranslationAdmin):
	class Media:
		js = (
			'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
			'modeltranslation/js/tabbed_translation_fields.js',
		)
		css = {
			'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		}


@admin.register(CaruselModel)
class CaruselModelAdmin(MyTranslationAdmin1):
	list_display = ['title', 'created_at']
	list_filter = ['created_at']
	search_fields = ['title', 'content']


@admin.register(ProductModel)
class ProductModelAdmin(MyTranslationAdmin1):
	list_display = ['title', 'created_at']
	list_filter = ['created_at']
	search_fields = ['title', 'short_description']


@admin.register(CallModel)
class CallModelAdmin(admin.ModelAdmin):
	list_display = ['call', 'created_at']
	list_filter = ['created_at']
	search_fields = ['call']
