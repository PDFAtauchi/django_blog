# Standard library imports

# Django framework
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

# Third party imports
import pytest


User = get_user_model()

pytestmark = pytest.mark.django_db

class RegisterAccountTest(TestCase):
    def setUp(self):
        self.register_account_url = reverse("register-account")
        self.login_url_redirect = reverse("login")
        self.client = Client()

    def tearDown(self):
        pass

    def test_account_register_get_request(self):
        # When
        response = self.client.get(self.register_account_url)

        # Then
        self.assertEqual(response.status_code, 200)

        # And
        template = 'users/register.html'
        self.assertTemplateUsed(response, template)

    def test_account_register_post_success(self):
        # Given
        data = {'username': "test",
                'email': "test@gmail.com",
                "password1": "1234Abcd@",
                "password2": "1234Abcd@"}

        # When
        response = self.client.post(self.register_account_url, data=data, format="json",)

        # Then
        self.assertRedirects(response, self.login_url_redirect, status_code=302,
                           target_status_code=200)

    def test_account_register_return_form_in_context(self):
        # When
        response = self.client.get(self.register_account_url)

        # Then
        form = response.context['form']
        self.assertTrue(isinstance(form.instance, User))


    def test_account_register_Post_errors(self):
        # Given
        data = {'username': "test",
                'email': "test@gmail.com",
                "password1": "1234",
                "password2": "1234"}

        # When
        response = self.client.post(self.register_account_url, data=data, format="json",)

        # Then
        self.assertEqual(response.status_code, 200)
        assert response.context["form"].errors["password2"][0] == "Esta contraseña es demasiado corta. Debe contener al menos 8 caracteres."
        assert response.context["form"].errors["password2"][1] == "Esta contraseña es demasiado común."
        assert response.context["form"].errors["password2"][2] == "Esta contraseña es completamente numérica."
