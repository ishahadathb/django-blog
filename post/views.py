from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

posts = Post.objects.all()


def home(request):
    context = {
        'posts': posts,
        'title': 'Shahadathb - Personal Blog'
    }
    return render(request, 'post/index.html', context)


class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/index.html'
    ordering = ['-posted_on']


class BlogDetails(DetailView):
    model = Post


class CreateBlog(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'post/about.html')
