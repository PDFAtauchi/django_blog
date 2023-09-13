# Django framework
from django.test import SimpleTestCase
from django.urls import resolve, reverse

# Local application imports
from apps.blog.views import PostListView, about


class HomePageTest(SimpleTestCase):
    def test_home_page(self):
        url = reverse("home-page")
        class_found = resolve(url).func.view_class
        assert class_found == PostListView

class AboutPageTest(SimpleTestCase):
    def test_about_page(self):
        url = reverse("about-page")
        function_found = resolve(url).func
        assert function_found == about
