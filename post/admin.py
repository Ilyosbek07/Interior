from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from post.models import PostModel, PostTagModel, CommentModel, CategoryModel


class MyTranslationAdmin2(TranslationAdmin):
	class Media:
		js = (
			'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
			'modeltranslation/js/tabbed_translation_fields.js',
		)
		css = {
			'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		}


@admin.register(PostModel)
class PostModelAdmin(MyTranslationAdmin2):
	search_fields = ['title', 'content']
	list_filter = ['created_at']
	list_display = ['title', 'content']
	autocomplete_fields = ['tags', 'category']


@admin.register(PostTagModel)
class PostTagModelAdmin(MyTranslationAdmin2):
	search_fields = ['title']
	list_filter = ['created_at']
	list_display = ['title']


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin2):
	search_fields = ['title']
	list_filter = ['created_at']
	list_display = ['title']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_at']
	list_filter = ['created_at']
	search_fields = ['name', 'comment']
