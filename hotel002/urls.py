from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('ckeditor/', include('ckeditor_uploader.urls')),
	path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += i18n_patterns(
	path('accaunts/', include('registration.backends.default.urls')),
	path('admin/', admin.site.urls),
	path('service/', include('service.urls', namespace='service')),
	path('profile1/', include('users.urls', namespace='profile1')),
	path('order/', include('order.urls', namespace='order')),
	path('post/', include('post.urls', namespace='post')),
	path('', include('products.urls', namespace='products')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
