# Django framework
from django.test import SimpleTestCase
from django.urls import resolve, reverse

# Local application imports
from apps.users.views import register


class RegisterUrlTest(SimpleTestCase):
    def test_register_url(self):
        url = reverse("register-account")
        function_found = resolve(url).func
        assert function_found == register
