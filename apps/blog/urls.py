# Django framework
from django.urls import path

# Local application imports
from apps.blog import views
from apps.blog.views import PostDetailView, PostListView


urlpatterns = [
    path("", PostListView.as_view(), name="home-page"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("about/", views.about, name="about-page"),
]
