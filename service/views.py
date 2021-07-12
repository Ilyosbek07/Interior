from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, ListView, DetailView

from products.models import ProductModel
from service.forms import ContactModelForm
from service.models import TeamModel, ServiceModel, StoryModel


class ContactCreatView(CreateView):
	form_class = ContactModelForm
	template_name = 'contact.html'

	def get_success_url(self):
		return reverse('service:contact')


class AboutTemplateView(TemplateView):
	template_name = 'about.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['teams'] = TeamModel.objects.order_by('-pk')
		# context['interiers'] = ServiceModel.objects.order_by('pk')
		context['stories'] = StoryModel.objects.order_by('pk')

		return context


class OffisInterierTemplateView(TemplateView):
	template_name = 'office-interior.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['interiers'] = ServiceModel.objects.order_by('-pk')

		return context


class ShopListView(ListView):
	template_name = 'shop.html'
	queryset = ProductModel.objects.order_by('pk')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['product'] = ProductModel.objects.order_by('pk')

		return context


class ShopDetailView(DetailView):
	template_name = 'shop-detail.html'
	model = ProductModel
