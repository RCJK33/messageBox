from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostDeleteView

urlpatterns = [
    path("/", PostListView.as_view(), name="list"),
    path("/<int:pk>", PostDetailView.as_view(), name="detail"),
    path("new/", PostCreateView.as_view(), name="new"),
    path("<int:pk>", PostDeleteView.as_view(), name="delete"),
]