# Django framework
from django.contrib.auth import get_user_model

# Third party imports
import factory


User = get_user_model()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    password = factory.PostGenerationMethodCall('set_password', 'random_password')
