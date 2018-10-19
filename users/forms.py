# -*- coding:utf-8 -*-
__author__ = 'yewei'
from django import forms
from django.contrib import auth

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名或邮箱',widget=forms.TextInput(
                                attrs={'class':'form-control', 'placeholder':'请输入用户名或邮箱'}),
                               required=True)
    password = forms.CharField(label='密码',widget=forms.PasswordInput(
                                attrs={'class':'form-control'}
                                ),
                               required=True, min_length=5)


    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码错误！')
        else:
            self.cleaned_data['user'] = user

        return self.cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        max_length=30,
        min_length=3,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'请输入3-30位用户名'})
    )
    email = forms.EmailField(
        label='邮箱',
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'请输入邮箱'})
    )
    verification_code = forms.CharField(
        label='验证码',
        required=False,
        widget=forms.TextInput(
            attrs={'class':'form-control', 'placeholder':'点击“发送验证码”发送到邮箱'}
        )
    )
    password = forms.CharField(
        label='密码',
        min_length=6,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'请输入密码'})
    )
    password_again = forms.CharField(
        label='再输入一次密码',
        min_length=6,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'再输入一次密码'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserProfile.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.objects.filter(email=email).exists():
            raise forms.ValidationError('该邮箱已被注册过')
        return email

    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次密码输入不一致')
        return password_again
