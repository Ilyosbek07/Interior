from django.urls import path

from users.views import ProfileUpdateView, HistoryTemplateView

app_name = 'profile1'

urlpatterns = [
    path('', ProfileUpdateView.as_view(), name='home'),
    path('history/', HistoryTemplateView.as_view(), name='history'),
]
