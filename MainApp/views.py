from django.shortcuts import render, HttpResponse
from .models import Post, Category


def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    model = {
        "posts": posts,
        "categories": categories
    }

    return render(request, "index.html", model)