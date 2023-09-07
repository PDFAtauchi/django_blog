# Django framework
from django.urls import path

# Local application imports
from apps.blog import views


urlpatterns = [
    path("", views.home, name="home-page"),
    path("about/", views.about, name="about-page"),
]
