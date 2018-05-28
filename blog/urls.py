from django.urls import path, include, re_path
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    re_path('^$', ListView.as_view(queryset= Post.objects.all().order_by("-date")[:25],
    template_name = 'blog/blog.html')),
    re_path('^(?P<pk>\d+)$',DetailView.as_view(model = Post,
    template_name='blog/post.html'))
    # $ notes the end of the url and there cannot be no more additions to the url
]