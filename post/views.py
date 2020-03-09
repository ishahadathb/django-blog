from django.shortcuts import render
from .models import Post
# Create your views here.

posts = Post.objects.all()


def home(request):
    context = {
        'posts': posts,
        'title': 'Shahadathb - Personal Blog'
    }
    return render(request, 'post/index.html', context)


def about(request):
    return render(request, 'post/about.html')
