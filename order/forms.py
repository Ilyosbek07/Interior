from django import forms

from order.models import OrderModel


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        exclude = ['created_at', 'user', 'service']
