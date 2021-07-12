from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from service.models import ServiceModel, TeamModel, ContactModel, StoryModel, AwesomePlaceModel


class MyTranslationAdmin(TranslationAdmin):
	class Media:
		js = (
			'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
			'modeltranslation/js/tabbed_translation_fields.js',
		)
		css = {
			'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		}


@admin.register(ServiceModel)
class ServiceModelAdmin(MyTranslationAdmin):
	list_display = ['title', 'created_at']
	list_filter = ['created_at']
	search_fields = ['title', 'content']


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_at']
	list_filter = ['created_at']
	search_fields = ['name', 'email']


@admin.register(TeamModel)
class TeamModelAdmin(MyTranslationAdmin):
	list_display = ['name', 'created_at']
	list_filter = ['created_at']
	search_fields = ['name', 'job']


@admin.register(StoryModel)
class StoryModelAdmin(MyTranslationAdmin):
	list_display = ['title', 'created_at']
	list_filter = ['created_at']
	search_fields = ['title', 'content']


@admin.register(AwesomePlaceModel)
class AwesomePlaceModelAdmin(MyTranslationAdmin):
	list_display = ['title', 'created_at']
	list_filter = ['created_at']
	search_fields = ['title', 'content']
