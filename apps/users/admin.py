# Django framework
from django.contrib import admin

# Local application imports
from apps.users.models import Profile


admin.site.register(Profile)
