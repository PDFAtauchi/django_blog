# Django framework
from django.test import Client, TestCase
from django.urls import reverse

# Third party imports
import pytest


pytestmark = pytest.mark.django_db

class HomePageTest(TestCase):

    def setup_class(self):
        self.home_page_url = reverse("home-page")
        self.client = Client()

    def tearDown(self):
        pass

    def test_home_page_return_title(self):
        # When
        response = self.client.get(self.home_page_url)

        # Then
        self.assertEquals(response.status_code, 200)

        # And
        template = 'blog/home.html'
        self.assertTemplateUsed(response, template)
