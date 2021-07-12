from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class StoryModel(models.Model):
	title = models.CharField(max_length=255, verbose_name=_('title'))
	content = models.CharField(max_length=255, verbose_name=_('content'))
	long_description = RichTextUploadingField(verbose_name=_('long_description'))
	image = models.ImageField(null=True, verbose_name=_('image'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('story')
		verbose_name_plural = _('stories')


class ServiceModel(models.Model):
	title = models.CharField(max_length=255, verbose_name=_('title'))
	content = models.CharField(max_length=255, verbose_name=_('content'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('service')
		verbose_name_plural = _('services')


class TeamModel(models.Model):
	name = models.CharField(max_length=255, verbose_name=_('name'))
	short_description = RichTextUploadingField(verbose_name=_('content'))
	job = models.CharField(max_length=55, verbose_name=_('job'))
	image1 = models.ImageField(null=True, verbose_name=_('image'))
	image2 = models.ImageField(null=True)

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('team')
		verbose_name_plural = _('teams')


class ContactModel(models.Model):
	name = models.CharField(max_length=50, verbose_name=_('name'))
	email = models.EmailField(verbose_name=_('email'))
	message = models.TextField(verbose_name=_('message'))
	phone = models.CharField(max_length=25, verbose_name=_('phone'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('contact')
		verbose_name_plural = _('contacts')


class AwesomePlaceModel(models.Model):
	title = models.CharField(max_length=55, verbose_name=_('title'))
	content = models.CharField(max_length=255, verbose_name=_('content'))
	image = models.ImageField(null=True, verbose_name=_('image'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('awesome place')
		verbose_name_plural = _('awesome places')
