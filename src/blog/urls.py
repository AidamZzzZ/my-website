from django.urls import path
from .views import ListPostView, CreatePostView, DetailPostView, DeletePostView, UpdatePostView

urlpatterns = [
    path('', ListPostView.as_view(), name="home"),
    path('create/', CreatePostView.as_view(), name="create"),
    path('<int:pk>/post/', DetailPostView.as_view(), name="detail"),
    path('<int:pk>/post/delete', DeletePostView.as_view(), name="delete"),
    path('<int:pk>/post/update', UpdatePostView.as_view(), name="update")
]
