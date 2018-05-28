from django.urls import path, include, re_path
from .import views

# The new path() syntax in Django 2.0 does not use regular expressions. You want something like:
# path('<int:album_id>/', views.detail, name='detail'),
# If you want to use a regular expression, you can use re_path().
# re_path(r'^(?P<album_id>[0-9])/$', views.detail, name='detail'),
# The old url() still works and is now an alias to re_path, but it is likely to be deprecated in future.
# url(r'^(?P<album_id>[0-9])/$', views.detail, name='detail'),

urlpatterns = [
    re_path('^$', views.index, name='index')
]
