# Standard library imports
import io

# Django framework
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

# Local application imports
from apps.users.models import Profile

# Third party imports
import pytest

from PIL import Image


User = get_user_model()

pytestmark = pytest.mark.django_db

class TestProfileModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com')
        self.user.set_password("123")
        self.user.save()

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
