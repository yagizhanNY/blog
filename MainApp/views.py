from django.shortcuts import render, HttpResponse
from .models import Post, Category


def index(request):
    posts = Post.objects.all()

    model = {
        "posts": posts
    }

    return render(request, "index.html", model)