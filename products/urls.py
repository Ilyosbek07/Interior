from django.urls import path

from products.views import HomeTemplateView, ServiceTemplateView, CardListView, add_to_card

app_name = 'products'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('interior/', ServiceTemplateView.as_view(), name='interior'),
    path('card/', CardListView.as_view(), name='card'),
    path('card/<int:pk>', add_to_card, name='add-to-card'),
    # path('add_to_card/<int:pk>', add_to_card, name='add_to_card'),
]
