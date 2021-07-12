from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from post.models import PostModel
from products.models import CaruselModel, ProductModel, CallModel
from service.models import ServiceModel, TeamModel, AwesomePlaceModel


class HomeTemplateView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['carusels'] = CaruselModel.objects.order_by('-pk')
		context['posts'] = AwesomePlaceModel.objects.order_by('pk')
		context['interiers'] = ServiceModel.objects.order_by('pk')
		context['teams'] = TeamModel.objects.order_by('pk')

		return context


class ServiceTemplateView(TemplateView):
	template_name = 'services-dark.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['posts'] = PostModel.objects.order_by('-pk')

		return context


class CallDetailView(DetailView):
	template_name = 'layouts/header.html'
	model = CallModel
	context_object_name = 'number'


class CardListView(LoginRequiredMixin, ListView):
	template_name = 'card.html'

	def get_queryset(self):
		return ProductModel.get_from_cart(self.request)


# @login_required
def add_to_card(request, pk):
	cart = request.session.get('cart', [])

	if pk in cart:
		cart.remove(pk)
	else:
		cart.append(pk)

	request.session['cart'] = cart

	return redirect(request.GET.get('next', '/'))
