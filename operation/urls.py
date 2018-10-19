# -*- coding:utf-8 -*-
__author__ = 'yewei'

from django.urls import path

from .views import AddCommentsView , AddLikeView

urlpatterns = [
	path('addcomment',AddCommentsView.as_view(),name='addcomment'),
	path('addlike',AddLikeView.as_view(),name='addlike'),
]

