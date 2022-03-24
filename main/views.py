from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from main.models import Post, Blog


class MainView(ListView):
    model = Post
    context_object_name = 'posts'

    def get(self, request, *args, **kwargs):
        qs = Post.objects.filter(is_published=True).order_by('-id')
        kwargs['posts'] = qs

        name = Blog.objects.all()[0]

        kwargs['name'] = Blog.objects.all()[0]
        return render(request, "blog/main.html", kwargs)


class ShowPost(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
