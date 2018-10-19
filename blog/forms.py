# -*- coding:utf-8 -*-
__author__ = 'yewei'

from django import forms


class QuestionForms(forms.Form):
	anwser = forms.CharField()
	question = forms.CharField()


class SearchForms(forms.Form):
	search_keywords = forms.CharField()