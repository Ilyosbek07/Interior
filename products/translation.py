from modeltranslation.translator import register, TranslationOptions

from products.models import CaruselModel, ProductModel


@register(CaruselModel)
class CaruselTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(ProductModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'long_description',)
