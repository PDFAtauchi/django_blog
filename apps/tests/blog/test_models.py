# Django framework
from django.test import TestCase
from django.urls import reverse

# Local application imports
from apps.blog.models import Post
from apps.tests.factories.users import UserFactory

# Third party imports
import pytest


pytestmark = pytest.mark.django_db

class TestPostModel(TestCase):
    def setUp(self):
        super().setUp()
        self.author = UserFactory()

    def tearDown(self):
        super().tearDown()

    def test_post_save(self):
        # Given
        post = Post(title="Blog Post 1", author_id=self.author.id)

        # When
        post.save()

        # Then
        self.assertEqual(post.title, "Blog Post 1")
        self.assertEqual(post.__str__(), "Blog Post 1")

    def test_post_retrieve(self):
        # Given
        post = Post(title="Blog Post 1", author_id=self.author.id)
        post.save()

        # When
        post = Post.objects.filter(
            pk=post.pk).first()

        # Then
        self.assertEqual(post.title, "Blog Post 1")

    def test_post_update(self):
        # Given
        post = Post(title="Blog Post 1", author_id=self.author.id)
        post.save()

        # When
        post = Post.objects.filter(
            pk=post.pk).first()
        self.assertEqual(post.title, "Blog Post 1")

        # And
        post.title = "Blog Post 2"
        post.save()

        # Then
        self.assertEqual(post.title, "Blog Post 2")

    def test_post_delete(self):
        # Given
        post = Post(title="Blog Post 1", author_id=self.author.id)
        post.save()

        # When
        post = Post.objects.filter(
            pk=post.pk).first()

        # Then
        self.assertIsNotNone(post)

        # And, When
        Post.objects.filter(pk=post.pk).delete()
        post = Post.objects.filter(
            pk=post.pk).first()

        # Then
        self.assertIsNone(post)

    def test_post_list(self):
        # Given
        posts = ["Blog Post 1", "Blog Post 2"]

        # When
        for i, title in enumerate(posts):
            Post(title=title, author_id=self.author.id).save()

        # Then
        posts_count = Post.objects.all().count()
        self.assertEqual(posts_count, len(posts))

    def test_get_absolute_url(self):
        # Given
        post = Post(title="Blog Post 1", author_id=self.author.id)

        # When
        post.save()

        # Then
        expected_url = reverse('post-detail', kwargs={'pk': post.pk})
        assert post.get_absolute_url() == expected_url
