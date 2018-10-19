# _*_ encoding:utf8 _*_
from django.urls import path

from blog.views import BlogDetailView,BlogListView


urlpatterns = [
    path('<int:blog_pk>',BlogDetailView.as_view(),name='blog_detail'),
    path('type/<int:blog_type_pk>',BlogListView.as_view(),name='blog_with_type'),
]
