from modeltranslation.translator import register, TranslationOptions

from post.models import PostModel, PostTagModel, CategoryModel


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
	fields = ('title', 'content', 'post_detail')


@register(PostTagModel)
class PostTagTranslationOptions(TranslationOptions):
	fields = ('title',)


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
	fields = ('title',)
