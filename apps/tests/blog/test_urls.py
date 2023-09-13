# Django framework
from django.test import SimpleTestCase
from django.urls import resolve, reverse

# Local application imports
from apps.blog.views import PostDetailView, PostListView, about


class HomePageTest(SimpleTestCase):
    def test_home_page(self):
        url = reverse("home-page")
        class_found = resolve(url).func.view_class
        assert class_found == PostListView

class PostDetailTest(SimpleTestCase):
    def test_post_detail(self):
        url = reverse("post-detail", kwargs={"pk": 1})
        class_found = resolve(url).func.view_class
        assert class_found == PostDetailView

class AboutPageTest(SimpleTestCase):
    def test_about_page(self):
        url = reverse("about-page")
        function_found = resolve(url).func
        assert function_found == about
