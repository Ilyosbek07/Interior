from django.urls import path

from service.views import ContactCreatView, AboutTemplateView, \
    OffisInterierTemplateView, ShopListView, ShopDetailView

app_name = 'service'

urlpatterns = [
    path('', ContactCreatView.as_view(), name='contact'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('offis/', OffisInterierTemplateView.as_view(), name='office'),
    path('shop/', ShopListView.as_view(), name='shop'),
    path('pro/<int:pk>/', ShopDetailView.as_view(), name='pro'),
]
