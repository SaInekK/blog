from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from main.forms import BlogNameForm
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


class UpdatePost(UpdateView):
    model = Post
    fields = [
        "title", "content", "is_published"
    ]
    template_name = "blog/update.html"
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        return super(UpdatePost, self).form_valid(form)


class DeletePost(DeleteView):
    model = Post
    template_name = "blog/delete.html"
    success_url = reverse_lazy("main")
    success_message = "The record was removed successfully!"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        data = super(DeletePost, self).delete(request, *args, **kwargs)
        return data


class CreatePost(CreateView):
    model = Post
    template_name = 'blog/create.html'
    fields = ["title", "content", "is_published"]
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        return super(CreatePost, self).form_valid(form)


class UpdateBlogName(UpdateView):
    model = Blog
    fields = [
        "name",
    ]
    template_name = "blog/update.html"
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        return super(UpdateBlogName, self).form_valid(form)

# class UpdateBlogName(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'blog/update.html', {'form': BlogNameForm()})
#
#     def post(self, request, *args, **kwargs):
#         form = BlogNameForm(data=request.POST)
#         if form.is_valid():
#             name = form.cleaned_data.get('name')
#         success_url = reverse_lazy('main')
#         return render(request, 'blog/update.html', {'form': form, 'name': name})

