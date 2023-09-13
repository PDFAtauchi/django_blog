# Django framework
from django.test import Client, TestCase
from django.urls import reverse

# Third party imports
import pytest


pytestmark = pytest.mark.django_db

class AboutPageTest(TestCase):

    def setUp(self):
        super().setUp()
        self.about_page_url = reverse("about-page")
        self.client = Client()

    def tearDown(self):
        super().tearDown()

    def test_about_page_return_title(self):
        # When
        response = self.client.get(self.about_page_url)

        # Then
        self.assertEquals(response.status_code, 200)

        # And
        template = 'blog/about.html'
        self.assertTemplateUsed(response, template)
