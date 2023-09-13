# Django framework
from django.urls import path

# Local application imports
from apps.blog import views
from apps.blog.views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)


urlpatterns = [
    path("", PostListView.as_view(), name="home-page"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="about-page"),
]
