from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from post.form import CommentModelForm
from post.models import PostModel, CategoryModel, PostTagModel


# if price:
#     price_from, price_to = price.split(';')
#     qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

# if sort:
#     if sort == 'price':
#         qs = qs.order_by('real_price')
#     elif sort == '-price':
#         qs = qs.order_by('-real_price')


class PostListView(ListView):
	template_name = 'blog.html'
	paginate_by = 1

	def get_queryset(self):
		qs = PostModel.objects.order_by('-pk')
		q = self.request.GET.get('q', None)
		tag = self.request.GET.get('tag')
		cat = self.request.GET.get('cat')

		if q:
			qs = qs.filter(title__icontains=q)

		if tag:
			qs = qs.filter(tags__title=tag)

		if cat:
			qs = qs.filter(category__title=cat)
		return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['blogs'] = PostModel.objects.order_by('pk')
		context['categories'] = CategoryModel.objects.order_by('pk')
		context['tags'] = PostTagModel.objects.order_by('pk')

		return context


class PostDetailView(DetailView):
	template_name = 'blog-detail.html'
	model = PostModel


class CommentCreateView(CreateView):
	form_class = CommentModelForm

	def form_valid(self, form):
		form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('post:detail', kwargs={'pk': self.kwargs.get('pk')})
