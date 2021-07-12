from django.urls import path, include

from auth1.views import password_changed

app_name = 'auth1'

urlpatterns = {
	path('accounts/change/done/', password_changed),
	path('', include('registration.backends.default.urls'))
}
