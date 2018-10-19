# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row
from django.utils.translation import ugettext as _

from .models import UserLike, Comment, UserCollect, UserArticle


class UserArticleAdmin(object):
    list_display = ['user', 'article_id', 'add_time']
    search_fields = ['user', 'article_id']
    list_filter = ['user', 'article_id', 'add_time']


class UserLikeAdmin(object):
    list_display = ['user', 'add_time', 'content_type', 'content_object', 'object_id']
    search_fields = ['user', 'content_type', 'content_object', 'object_id']
    list_filter = ['user', 'add_time', 'content_type', 'content_object', 'object_id']


class UserCollectAdmin(object):
    list_display = ['user', 'add_time', 'content_type', 'content_object', 'object_id']
    search_fields = ['user', 'content_type', 'content_object', 'object_id']
    list_filter = ['user', 'add_time', 'content_type', 'content_object', 'object_id']


class CommentAdmin(object):
    list_display = ['content', 'user', 'content_type', 'comment_time', 'object_id', 'content_object']
    search_fields = ['content', 'user', 'content_type', 'comment_time', 'object_id']
    list_filter = ['content', 'user', 'content_type', 'comment_time', 'object_id', 'content_object']


#
xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(UserCollect, UserCollectAdmin)
xadmin.site.register(UserLike, UserLikeAdmin)
xadmin.site.register(UserArticle, UserArticleAdmin)