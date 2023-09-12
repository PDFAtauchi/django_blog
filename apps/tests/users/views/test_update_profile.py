# Standard library imports

# Django framework
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

# Third party imports
import pytest


User = get_user_model()

pytestmark = pytest.mark.django_db

class ProfileUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword', email='test@example.com')

        self.profile_account_url = reverse("profile-account")
        self.login_url_unauthenticated_redirect = reverse('login') + f'?next={reverse("profile-account")}'
        self.client = Client()

    def tearDown(self):
        self.user.delete()

    def test_get_profile_view_unauthenticated(self):
        # When
        response = self.client.get(self.profile_account_url)

        # Then
        self.assertRedirects(response, self.login_url_unauthenticated_redirect, status_code=302,
                           target_status_code=200)


    def test_profile_update_account_post_success(self):
        # Given
        self.client.login(username='testuser', password='testpassword')

        user_data = {'username': "test",
                'email': "test@gmail.com"}
        profile_data = {'image': "image-mock"}
        data = {**user_data, **profile_data}
        # When
        response = self.client.post(self.profile_account_url, data=data, format="json")

        # Then
        self.assertRedirects(response, self.profile_account_url, status_code=302,
                           target_status_code=200)

    def test_profile_update_account_post_errors(self):
        # Given
        self.client.login(username='testuser', password='testpassword')

        user_data = {'username': "",
                'email': "test@gmail.com"}
        profile_data = {'image': "image-mock"}
        data = {**user_data, **profile_data}
        # When
        response = self.client.post(self.profile_account_url, data=data, format="json")

        # Then
        user_form = response.context["user_form"]
        assert response.status_code == 200
        assert user_form.errors["username"][0] == "Este campo es obligatorio."

    # def test_profile_image_resize_test(self):
    #     # Given
    #     image = Image.new('RGB', (700, 700))
    #     image_io = io.BytesIO()
    #     image.save(image_io, 'JPEG')

    #     self.client.login(username='testuser', password='testpassword')
    #     image_file = SimpleUploadedFile("test_image.jpg", image_io.getvalue(), content_type="image/jpeg")

    #     user_data = {'username': "test",
    #             'email': "test@gmail.com"}
    #     profile_data = {'image': image_file}
    #     data = {**user_data, **profile_data}

    #     # When
    #     response = self.client.post(self.profile_account_url, data=data, format="json")

    #     # Then
    #     self.assertRedirects(response, self.profile_account_url, status_code=302,
    #                        target_status_code=200)
