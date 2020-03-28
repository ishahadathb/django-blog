from django.shortcuts import render, get_list_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.views import View
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
    paginate_by = 2


class BlogDetails(DetailView):
    model = Post


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class DeleteBlog(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'


def UserBlogListView(request, username):
    user = User.objects.get(username=username)
    user_posts = get_list_or_404(Post, author=user)

    paginator = Paginator(user_posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post/user_posts.html', {'posts': page_obj.object_list, 'page_obj': page_obj, 'user': username})


def about(request):
    return render(request, 'post/about.html')
