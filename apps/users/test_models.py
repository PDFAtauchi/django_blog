# Standard library imports

# Django framework
from django.contrib.auth import get_user_model
from django.test import TestCase

# Third party imports
import pytest


User = get_user_model()

pytestmark = pytest.mark.django_db

class TestProfileModel(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
