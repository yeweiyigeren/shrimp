# _*_ encoding:utf8 _*_
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from users.models import UserProfile
from blog.models import Blog


# Create your models here.
class Comment(models.Model):
	content = models.TextField(verbose_name=u'评论内容')
	blog = models.ForeignKey(Blog, verbose_name=u'博客', on_delete=models.CASCADE)
	comment_time = models.DateTimeField(auto_now_add=True,verbose_name=u'评论时间')
	user = models.ForeignKey(UserProfile,verbose_name=u'用户',on_delete=models.CASCADE)


	root = models.ForeignKey('self', related_name='root_comment', null=True, on_delete=models.CASCADE)
	parent = models.ForeignKey('self', related_name='parent_comment', null=True, on_delete=models.CASCADE)
	reply_to = models.ForeignKey(UserProfile, related_name="replies", null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.text

	class Meta:
		ordering = ['comment_time']
		verbose_name = u'评论'
		verbose_name_plural = verbose_name


class UserCollect(models.Model):
	user = models.ForeignKey(UserProfile,verbose_name=u'用户',on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog,verbose_name=u'博客',on_delete=models.CASCADE)
	add_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = u'用户收藏'
		verbose_name_plural = verbose_name


class UserLike(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
	blog = models.ForeignKey(Blog, verbose_name=u'博客', on_delete=models.CASCADE)
	add_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = u'用户点赞'
		verbose_name_plural = verbose_name


class UserArticle(models.Model):
	user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
	article = models.ForeignKey(Blog, verbose_name=u'文章id', on_delete=models.CASCADE)
	add_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = u'我的文章'
		verbose_name_plural = verbose_name

