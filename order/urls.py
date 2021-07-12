from django.urls import path

from order.views import OrderCreateView

app_name = 'order'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create')
]
