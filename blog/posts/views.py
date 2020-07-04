from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import title
from django.urls import reverse

from .models import Post
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from .forms import CommentForm
from .forms import forms


def index(request):
    featured = Post.objects.all()
    latest = Post.objects.order_by('-timestamp')[0:3]

    context = {'object_list': featured,
               'latest': latest
               }
    return render(request, 'index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'featured'


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post

    fields = ['title', 'description', 'author','genre']


def blog(request):
    postList = Post.objects.all()
    context = {
        'postList': postList
    }
    return render(request, 'blog.html', context)


def post(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
    context = {
        'post': post,
        'form': form
    }
    return redirect((reverse("post_details", kwargs={'id': post.pk})))


def post_detail(request, title):
    post = Post.objects.get(title=title)
    return render(request, 'posts/post_detail.html', {'post': post})
