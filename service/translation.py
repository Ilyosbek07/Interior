from modeltranslation.translator import register, TranslationOptions

from service.models import ServiceModel, TeamModel, StoryModel, AwesomePlaceModel


@register(ServiceModel)
class PostTranslationOptions(TranslationOptions):
	fields = ('title', 'content',)


@register(AwesomePlaceModel)
class AwesomePlaceTranslationOptions(TranslationOptions):
	fields = ('title', 'content',)


@register(TeamModel)
class PostTranslationOptions(TranslationOptions):
	fields = ('short_description',)


@register(StoryModel)
class StoryTranslationOptions(TranslationOptions):
	fields = ('title', 'content', 'long_description',)
