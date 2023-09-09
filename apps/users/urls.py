# Django framework
from django.urls import path

# Local application imports
from apps.users import views


urlpatterns = [
    path("register/", views.register, name="register-account"),
]
