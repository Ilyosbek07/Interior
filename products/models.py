from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CaruselModel(models.Model):
	title = models.CharField(max_length=255, verbose_name=_('title'))
	content = models.CharField(max_length=255, verbose_name=_('content'))
	image = models.ImageField(null=True, verbose_name=_('image'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('carusel')
		verbose_name_plural = _('carusels')


class CallModel(models.Model):
	call = models.CharField(max_length=25, verbose_name=_('call'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.call

	class Meta:
		verbose_name = _('call')


class ProductModel(models.Model):
	title = models.CharField(max_length=25, verbose_name=_('title'))
	short_description = models.TextField(null=True)
	long_description = RichTextField(verbose_name=_('content'))
	image = models.ImageField(null=True, verbose_name=_('image'))
	price = models.FloatField(verbose_name=_('price'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	@staticmethod
	def get_from_cart(request):
		cart = request.session.get('cart', [])
		return ProductModel.objects.filter(
			pk__in=cart
		)

	class Meta:
		verbose_name = _('product')
		verbose_name_plural = _('products')
