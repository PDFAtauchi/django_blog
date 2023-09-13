# Django framework
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

# Local application imports
from apps.blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/about.html')
