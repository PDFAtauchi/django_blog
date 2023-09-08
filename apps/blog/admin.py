# Django framework
from django.contrib import admin

# Local application imports
from apps.blog.models import Post


admin.site.register(Post)
