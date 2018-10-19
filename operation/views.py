from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

from .models import Comment,UserLike
from .forms import CommentForm
from blog.models import Blog


class AddCommentsView(View):
	def post(self,request):
		blog_id = request.POST.get('blog_id',0)
		comments = request.POST.get('comments','')

		if request.user.is_authenticated:
			if int(blog_id) > 0 and comments:
				blog_comment = Comment()
				blog = Blog.objects.get(id=blog_id)
				blog_comment.blog = blog
				blog_comment.content = comments
				blog_comment.user = request.user
				blog_comment.save()
				return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
			else:
				return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')
		else:
			return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')


class AddLikeView(View):
	def post(self,request):
		blog_id = request.POST.get('blog_id',0)

		if request.user.is_authenticated:
			blog = Blog.objects.get(id=blog_id)
			user_like = UserLike.objects.filter(blog=blog,user=request.user)
			if user_like:
				user_like.delete()
			else:
				user_like = UserLike()
				user_like.blog = blog
				user_like.user = request.user
				user_like.save()
			return HttpResponse('{"status":"success", "msg":"修改成功"}', content_type='application/json')
		else:
			return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
