from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from django.views.static import serve
import xadmin

from users.views import IndexView,LoginView, RegisterView, LogoutView,SendVerificationCodeView
from .settings import MEDIA_ROOT,STATIC_ROOT
from blog.views import MyWorldView,QuestionView,SearchView

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('yzt/xadmin/', xadmin.site.urls),
    path('blog/',include('blog.urls')),
    path('operation/',include('operation.urls')),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('search/',SearchView.as_view(),name='search'),
    path('send_verification_code/',SendVerificationCodeView.as_view(),name='send_verification_code'),
    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$',  serve, {"document_root":STATIC_ROOT}),
    path('question/',QuestionView.as_view(),name='question'),
    path('ckeditor',include('ckeditor_uploader.urls')),
]

# #全局404页面配置
# handler404 = 'users.views.page_not_found'
#
# #全局500页面配置
# handler500 = 'users.views.page_error'