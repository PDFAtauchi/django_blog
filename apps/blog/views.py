# Django framework
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Local application imports
from apps.blog.models import Post


def home(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context)

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/about.html')
