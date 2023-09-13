# Django framework
from django.urls import path

# Local application imports
from apps.blog import views
from apps.blog.views import PostListView


urlpatterns = [
    path("", PostListView.as_view(), name="home-page"),
    path("about/", views.about, name="about-page"),
]
