# Django framework
from django.test import SimpleTestCase
from django.urls import resolve, reverse

# Local application imports
from apps.blog.views import about


class AboutPageTest(SimpleTestCase):
    def test_home_page(self):
        url = reverse("about-page")
        function_found = resolve(url).func
        assert function_found == about
