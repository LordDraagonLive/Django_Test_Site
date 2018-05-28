from django.urls import path, include, re_path
from .import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    # $ notes the end of the url and there cannot be no more additions to the url
    re_path('contact/$', views.contact, name='contact')
]