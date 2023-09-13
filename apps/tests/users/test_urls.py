# Django framework
from django.test import SimpleTestCase
from django.urls import resolve, reverse

# Local application imports
from apps.users.views import profile, register


class RegisterUrlTest(SimpleTestCase):
    def test_register_url(self):
        url = reverse("register-account")
        function_found = resolve(url).func
        assert function_found == register

    def test_profile_url(self):
        url = reverse("profile-account")
        function_found = resolve(url).func
        assert function_found == profile
