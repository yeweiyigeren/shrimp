"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(BASE_DIR , 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gk)7x3g7#v!^8qpk^tjwim6!txs_v7t*56b1fcb03)-qvpck2-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',
    'ckeditor',
    'ckeditor_uploader',
    'crispy_forms',
    'users',
    'blog',
    'operation',
]

AUTH_USER_MODEL = "users.UserProfile"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shrimp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'shrimp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': "myblog",
    #     'USER': 'root',
    #     'PASSWORD': "root",
    #     'HOST': "127.0.0.1"
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR , 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR , 'media/')

DATETIME_FORMAT = 'Y-m-d H:i:s'

#配置ckeditor
CKEDITOR_UPLOAD_PATH = 'upload/'


# 自定义参数
EACH_PAGE_BLOGS_NUMBER = 10


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'yeweiyigeren@163.com'
EMAIL_HOST_PASSWORD = 'YWhenxili520'  # 授权码
EMAIL_SUBJECT_PREFIX = '[Shrimp_in_the_sea] '
EMAIL_USE_SSL = True  # 与SMTP服务器通信时，是否启动ssl链接(安全链接)


ADMINS = (
    ('admin', '289333404@qq.com'),
)

# 日志文件
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            # 'filename': 'shrimp_debug.log',
            'filename': '/home/shrimp_debug/shrimp_debug.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

