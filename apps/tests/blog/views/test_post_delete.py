# Django framework
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# Local application imports
from apps.blog.models import Post

# Third party imports
import pytest


@pytest.mark.django_db
class PostCreateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.post = Post.objects.create(title="My Post", content="Content of my Post", author=self.user)

    def tearDown(self):
        if self.user:
            self.client.logout()

    def test_delete_post(self):
        # Given
        self.post_delete_url = reverse('post-delete', args=[self.post.pk])
        self.home_page_url = reverse('home-page')

        # When
        response = self.client.post(self.post_delete_url)
        self.assertRedirects(response, self.home_page_url, status_code=302,
                           target_status_code=200)

    def test_create_post_form_invalid(self):
        # Given
        self.user = User.objects.create_user(username='otheruser', password='testpassword')
        self.client.login(username='otheruser', password='testpassword')
        self.post_delete_url = reverse('post-delete', args=[self.post.pk])

        # When
        response = self.client.post(self.post_delete_url)

        # Then
        assert response.status_code == 403
