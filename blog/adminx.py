# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import BlogType,Blog


class BlogTypeAdmin(object):
    list_display = ['type_name', 'top_type']
    search_fields = ['type_name', 'top_type']
    list_filter = ['type_name', 'top_type']


class BlogAdmin(object):
    list_display = ['title', 'blog_type', 'author','read_num', 'thumb_img', 'create_time', 'update_time']
    search_fields = ['title', 'blog_type', 'author', 'thumb_img']
    list_filter = ['title', 'blog_type', 'author', 'thumb_img', 'create_time', 'update_time']
    # fields =  ('title', 'blog_type', 'author', 'content')


#
xadmin.site.register(BlogType, BlogTypeAdmin)
xadmin.site.register(Blog, BlogAdmin)
