# _*_ encoding:utf-8 _*_
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class UserProfile(AbstractUser):
	# user = models.OneToOneField(User, on_delete=models.CASCADE)
	nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
	birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
	gender = models.CharField(max_length=6, choices=(("male",u"男"),("female","女")), default="female")
	address = models.CharField(max_length=100, null=True, blank=True,default=u"")
	mobile = models.CharField(max_length=11, null=True, blank=True)
	image = models.ImageField(upload_to="user_image/%Y/%m",default=u"user_image/default.png", max_length=100)
	# create_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "用户信息"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.username


class EmailVerifyRecord(models.Model):
	code = models.CharField(max_length=20,verbose_name=u'验证码')
	email = models.EmailField(max_length=50,verbose_name=u'邮箱')
	send_type = models.CharField(choices=(("register",u"注册"),("forget",u"找回密码"), ("update_email",u"修改邮箱")),max_length=50,verbose_name=u'验证码类型')
	send_time = models.DateTimeField(auto_now_add=True,verbose_name=u'发送时间')

	class Meta:
		verbose_name = u'邮箱验证码'
		verbose_name_plural = verbose_name

	def __str__(self):
		return '{0}({1})'.format(self.code, self.email)








