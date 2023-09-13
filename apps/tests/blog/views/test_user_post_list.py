# Django framework
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

# Local application imports
from apps.blog.models import Post

# Third party imports
import pytest


User = get_user_model()

@pytest.mark.django_db
class UserPostListTest(TestCase):

    def setUp(self):
        super().setUp()
        self.user1 = User.objects.create_user(username='testuser1', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')

        self.post1 = Post.objects.create(title="My Post 1", content="Content of my Post 1", author=self.user1)
        self.post2 = Post.objects.create(title="My Post 2", content="Content of my Post 2", author=self.user2)

        self.client = Client()
        self.client.login(username='testuser1', password='testpassword')

    def tearDown(self):
        super().tearDown()

    def test_user_post_list(self):
        # When
        user_posts_list_url = reverse("user-posts", args=[self.user1.username])
        response = self.client.get(user_posts_list_url)

        # Then
        assert response.status_code == 200

        # And
        template = 'blog/user_posts.html'
        self.assertTemplateUsed(response, template)
