from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from django.views.static import serve
import xadmin

from users.views import IndexView,LoginView, RegisterView, LogoutView
from .settings import MEDIA_ROOT
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
    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('question/',QuestionView.as_view(),name='question'),
]
