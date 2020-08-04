from django.urls import path
from . import views

urlpatterns = [
    path('', views.read_blog_list, name='read_blog_list'),
]