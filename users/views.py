#encoding=utf-8
import random
import string
import time
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth.backends import ModelBackend
from django.urls import reverse
from django.db.models import Q
from django.core.mail import send_mail

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
		register_form = RegisterForm(request.POST,request=request)
		if register_form.is_valid():
			username = register_form.cleaned_data['username']
			email = register_form.cleaned_data['email']
			password = register_form.cleaned_data['password']

			user = UserProfile.objects.create_user(username,email,password)
			user.nick_name = username
			user.save()

			# 清除session
			# del request.session['register_code']

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


class SendVerificationCodeView(View):
	def get(self,request):
		email = request.GET.get('email', '')
		send_for = request.GET.get('send_for', '')
		data = {}

		if email != '':
			# 生成验证码
			code = ''.join(random.sample(string.ascii_lowercase + string.digits, 4))
			now = int(time.time())
			send_code_time = request.session.get('send_code_time', 0)
			if now - send_code_time < 30:
				data['status'] = 'ERROR'
			else:
				request.session[send_for] = code
				request.session['send_code_time'] = now
				print(request.session['register_code'])

				# 发送邮件
				send_mail(
					'验证码',
					'欢迎注册Shrimp_in_the_sea，验证码：%s （请注意字母大小写！）' % code,
					'Shrimp_in_the_sea<yeweiyigeren@163.com>',
					[email],
					fail_silently=False,
				)
				data['status'] = 'SUCCESS'
		else:
			data['status'] = 'ERROR'
		print(data)
		return JsonResponse(data)


def page_not_found(request):
    #全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

def page_error(request):
    #全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response

