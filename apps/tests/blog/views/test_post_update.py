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

    def test_update_post(self):
        # Given
        data = {
            'title': 'Test Post',
            'content': 'This is a test post content.'
        }

        # When
        self.post_update_url = reverse('post-update', args=[self.post.pk])
        response = self.client.post(self.post_update_url, data)

        # Then
        post_detail_url = reverse('post-detail', args=[self.post.pk])
        self.assertRedirects(response, post_detail_url, status_code=302,
                           target_status_code=200)

        # And
        updated_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(updated_post.author, self.user)
        self.assertEqual(updated_post.title, data["title"])
        self.assertEqual(updated_post.content, data["content"])

    def test_create_post_form_invalid(self):
        self.user = User.objects.create_user(username='otheruser', password='testpassword')
        self.client.login(username='otheruser', password='testpassword')

        # Given
        data = {
            'title': 'Test Post Updated',
            'content': 'This is a test post content Updated.'
        }

        # When
        self.post_update_url = reverse('post-update', args=[self.post.pk])
        response = self.client.post(self.post_update_url, data)

        # Then
        updated_post = Post.objects.get(pk=self.post.pk)
        assert updated_post == self.post

        # Then
        assert response.status_code == 403
