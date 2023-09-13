# Standard library imports
import io

# Django framework
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

# Local application imports
from apps.tests.factories.users import UserFactory
from apps.users.models import Profile

# Third party imports
from PIL import Image


class TestProfileModel(TestCase):
    def setUp(self):
        self.user = UserFactory(username=self.username)

    def tearDown(self):
        pass

    def test_profile_resize_image_save(self):
        # Given
        image = Image.new('RGB', (700, 700))
        image_io = io.BytesIO()
        image.save(image_io, 'JPEG')
        image_file = SimpleUploadedFile("test_image.jpg", image_io.getvalue(), content_type="image/jpeg")

        profile = Profile.objects.get(user_id=self.user.id)
        profile.image = image_file

        # When
        profile.save()

        # Then
        image_retrieved = Image.open(profile.image.path)
        self.assertEqual(image_retrieved.height, 300)
        self.assertEqual(image_retrieved.width, 300)
