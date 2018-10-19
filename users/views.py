#encoding=utf-8
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.backends import ModelBackend
from django.urls import reverse
from django.db.models import Q

from .models import UserProfile
from .forms import LoginForm ,RegisterForm

class IndexView(View):
	def get(self,request):
		return render(request , 'index.html')


class ListView(View):
	def get(self,request):
		return render(request, 'list.html')


class LoginView(View):
	def get(self,request):
		login_form = LoginForm()
		context = {}
		context['login_form'] = login_form
		if 'search' in request.META.get('HTTP_REFERER', '/'):
			request.session['login_from'] = ''
		else:
			request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
		return render(request, 'login.html',context)

	def post(self,request):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			user = login_form.cleaned_data['user']
			login(request,user)
			if request.session['login_from']:
				return redirect(request.session['login_from'])
			return render(request, "index.html")
		else:
			return render(request, "login.html", {"login_form": login_form})


class RegisterView(View):
	def get(self,request):
		register_form = RegisterForm()
		context = {}
		context['register_form'] = register_form
		if 'search' in request.META.get('HTTP_REFERER', '/'):
			request.session['register_form'] = ''
		else:
			request.session['register_form'] = request.META.get('HTTP_REFERER', '/')
		return render(request, 'register.html', context)

	def post(self,request):
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			username = register_form.cleaned_data['username']
			email = register_form.cleaned_data['email']
			password = register_form.cleaned_data['password']

			user = UserProfile.objects.create_user(username,email,password)
			user.nick_name = username
			user.save()

			user = authenticate(username=username,password=password)
			login(request,user)
			if request.session['register_form']:
				return redirect(request.session['register_form'])
			return render(request, "index.html")
		else:
			return render(request, "register.html", {"register_form": register_form})

class LogoutView(View):
	"""
	用户登出
	"""
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse("index"))