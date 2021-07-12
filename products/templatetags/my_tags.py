from django import template
from django.db.models import Sum

from products.models import ProductModel
from products.utils import get_card_lengs

register = template.Library()


@register.simple_tag
def get_lang_url(request, lang):
	url = request.path.split('/')
	url[1] = lang
	return '/'.join(url)


@register.filter
def in_cart1(object, request):
	return object.pk in request.session.get('cart', [])


@register.simple_tag
def count_card(request):
	return get_card_lengs(request)


@register.simple_tag
def card_price(request):
	if get_card_lengs(request) == 0:
		return 0

	return ProductModel.get_from_cart(request).aggregate(
		Sum('price')
	).get('price__sum', 0)
