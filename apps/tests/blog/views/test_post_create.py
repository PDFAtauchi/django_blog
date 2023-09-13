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
        self.post_create_url = reverse('post-create')

    def test_create_post(self):
        # Given
        data = {
            'title': 'Test Post',
            'content': 'This is a test post content.'
        }

        # When
        response = self.client.post(self.post_create_url, data)

        # Then
        post = Post.objects.get(author=self.user)
        post_detail_url = reverse('post-detail', args=[post.pk])
        self.assertRedirects(response, post_detail_url, status_code=302,
                           target_status_code=200)

        # And
        self.assertEqual(Post.objects.count(), 1)

        # And
        new_post = Post.objects.first()
        self.assertEqual(new_post.author, self.user)
        self.assertEqual(new_post.title, 'Test Post')
        self.assertEqual(new_post.content, 'This is a test post content.')

    def test_create_post_form_invalid(self):
        # Given
        data = {
            'title': '',
            'content': ''
        }

        # When
        response = self.client.post(self.post_create_url, data)

        # Then
        self.assertEqual(response.status_code, 200)

        # And
        self.assertEqual(Post.objects.count(), 0)
