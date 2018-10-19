# -*- coding:utf-8 -*-
__author__ = 'yewei'

from django import forms


class CommentForm(forms.Form):
	content_type = forms.CharField()
	object_if = forms.IntegerField()
	text = forms.CharField()

