from django.urls import path

from post.views import PostListView, PostDetailView, CommentCreateView

app_name = 'post'

urlpatterns = [
	path('', PostListView.as_view(), name='home'),
	path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
	path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
]
