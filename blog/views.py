from django.shortcuts import render,get_object_or_404
from django.views.generic.base import View
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
from django.http import HttpResponse

from .models import Blog,BlogType
from operation.models import Comment,UserLike
from .forms import QuestionForms,SearchForms


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = request.GET.get('page', 1) # 获取url的页面参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)
    currentr_page_num = page_of_blogs.number # 获取当前页码
    # 获取当前页码前后各2页的页码范围
    page_range = list(range(max(currentr_page_num - 2, 1), currentr_page_num)) + \
                 list(range(currentr_page_num, min(currentr_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    return context


class BlogDetailView(View):
	'''
	博客详情页
	'''
	def get(self,request,blog_pk):
		blog = get_object_or_404(Blog,pk=blog_pk)
		if blog.blog_type.pk == 10:
			if  not request.session.has_key('question'):
				return render(request, 'index.html')

		comments = Comment.objects.filter(blog=blog)
		like_num = UserLike.objects.filter(blog=blog).count()

		if request.user.is_authenticated:
			is_like = UserLike.objects.filter(blog=blog,user=request.user)
		else:
			is_like = False
		blog.read_num += 1
		blog.save()

		context = {}
		context['blog'] = blog
		context['like_num'] = like_num
		context['is_like'] = is_like
		context['comment_num'] = len(comments)
		context['comments'] = comments
		return render(request, 'detail.html',context)


class BlogListView(View):
	'''
	博客列表页
	'''
	def get(self,request,blog_type_pk):
		if blog_type_pk == 10:
			return render(request, 'index.html')
		blog_type = get_object_or_404(BlogType, pk=blog_type_pk)

		if not blog_type.top_type_id:
			sub_blogs = BlogType.objects.filter(top_type_id=blog_type_pk)
			all_blogs = Blog.objects.filter(blog_type__in=sub_blogs)
		else:
			sub_blogs = BlogType.objects.filter((Q(top_type_id=blog_type_pk)|Q(top_type_id=blog_type.top_type_id))&~Q(type_name=blog_type.type_name))
			all_blogs = Blog.objects.filter(blog_type=blog_type)

		context = get_blog_list_common_data(request, all_blogs)

		context['blog_type'] = blog_type
		context['sub_blogs'] = sub_blogs
		return render(request,'list.html',context)


class MyWorldView(View):
	def get(self,request):
		pass


class QuestionView(View):
	def get(self,request):
		question_form = QuestionForms()
		questions = [
			'请问世上最漂亮的人是?',
			'请问217代表什么?',
			'有一项运动我心仪已久，是什么?',
		]

		import random

		value = questions[random.randint(0,2)]
		context = {}
		context['question'] = value
		context['question_form'] = question_form
		return render(request, 'question.html', context)

	def post(self,request):
		question_form = QuestionForms(request.POST)
		if question_form.is_valid():
			anwser = request.POST.get("anwser", "")
			question = request.POST.get("question", "")

			questions = {
				'请问世上最漂亮的人是?':'女儿',
				'请问217代表什么?':'宿舍',
				'有一项运动我心仪已久，是什么?':'跳伞',
			}
			my_answer = questions[question]
			if my_answer == anwser:
				blog_type = get_object_or_404(BlogType, pk=10)
				all_blogs = Blog.objects.filter(blog_type=blog_type)
				context = get_blog_list_common_data(request, all_blogs)

				context['blog_type'] = blog_type
				request.session['question'] = True
				return render(request, 'srldlist.html', context)
			else:
				return render(request, "question.html", {"msg": "答案错误！",'question':question})
		else:
			return render(request, "question.html", {"question_form": question_form})


class SearchView(View):
	def post(self,request):
		search_form = SearchForms(request.POST)
		if search_form.is_valid():
			search_keywords = request.POST.get("search_keywords", "")

			if search_keywords:
				all_blogs = Blog.objects.filter(Q(title__icontains=search_keywords) | Q(content__icontains=search_keywords))

				context = get_blog_list_common_data(request, all_blogs)

				return render(request, 'searchlist.html', context)
			else:
				return render(request, 'index.html')
		else:
			return render(request, 'index.html')