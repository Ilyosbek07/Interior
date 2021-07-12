from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryModel(models.Model):
	title = models.CharField(max_length=55, verbose_name=_('title'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('category')
		verbose_name_plural = _('categories')


class PostTagModel(models.Model):
	title = models.CharField(max_length=55, verbose_name=_('title'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('post tag')
		verbose_name_plural = _('post tags')


class PostModel(models.Model):
	title = models.CharField(max_length=55, verbose_name=_('title'))
	image = models.ImageField(null=True, verbose_name=_('image'))
	content = RichTextUploadingField(null=True, verbose_name=_('content'))
	tags = models.ManyToManyField(
		PostTagModel,
		related_name='posts', verbose_name=_('tags')
	)
	category = models.ManyToManyField(
		CategoryModel,
		related_name='posts',
		verbose_name=_('category'),
	)
	post_detail = RichTextUploadingField(null=True, verbose_name=_('post detail'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	def get_comments(self):
		return self.comment.order_by('-created_at')

	def get_prev(self):
		return self.get_previous_by_created_at()

	def get_next(self):
		return self.get_next_by_created_at()

	class Meta:
		verbose_name = _('post')
		verbose_name_plural = _('posts')


class CommentModel(models.Model):
	post = models.ForeignKey(
		PostModel,
		related_name='comment',
		on_delete=models.CASCADE,
		verbose_name=_('post')
	)
	name = models.CharField(max_length=255, verbose_name=_('name'))
	email = models.EmailField(verbose_name=_('email'))
	phone = models.CharField(
		max_length=25, null=True, blank=True,
		verbose_name=_('phone'))
	comment = models.TextField(verbose_name=_('comment'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('comment')
		verbose_name_plural = _('comments')
