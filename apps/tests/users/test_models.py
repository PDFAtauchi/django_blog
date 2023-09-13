# Django framework
from django.test import TestCase

# Local application imports
from apps.tests.factories.users import UserFactory
from apps.users.models import Profile


class TestProfileModel(TestCase):
    def setUp(self):
        self.user = UserFactory(username="Tom")

    def tearDown(self):
        pass

    def test_profile_resize_image_save(self):
        # Given
        profile = Profile.objects.get(user_id=self.user.id)

        # Then
        self.assertEqual(profile.__str__(), f"{self.user.username} Profile")
