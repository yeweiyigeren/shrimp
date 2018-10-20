from datetime import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from users.models import UserProfile


class BlogType(models.Model):
	type_name = models.CharField(max_length=10, verbose_name=u'类型名称')
	nick_name = models.CharField(max_length=10, verbose_name=u'别称',null=True,blank=True)
	type_img = models.ImageField(upload_to='type/',default='type/default.png',verbose_name=u'缩略图')
	top_type = models.ForeignKey('self',null=True,blank=True,verbose_name=u'上级类型',on_delete=models.CASCADE)

	class Meta:
		verbose_name = u'博客类型'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.type_name


class Blog(models.Model):
	title = models.CharField(max_length=100,verbose_name=u'标题')
	blog_type = models.ForeignKey(BlogType, verbose_name=u'类型', on_delete=models.CASCADE)
	content = RichTextUploadingField(verbose_name=u'内容')
	author = models.ForeignKey(UserProfile, verbose_name=u'作者',on_delete=models.CASCADE)
	thumb_img = models.ImageField(upload_to='thumb/%m',default='',verbose_name=u'缩略图',null=True,blank=True)
	create_time = models.DateTimeField(auto_now_add=datetime.now(),verbose_name=u'创建时间')
	update_time = models.DateTimeField(auto_now=True, verbose_name=u'最后更新时间')
	read_num = models.IntegerField(verbose_name=u'阅读数',default=0)

	class Meta:
		verbose_name = u'文章'
		verbose_name_plural = verbose_name
		ordering = ['-create_time']

	def __str__(self):
		return self.title




