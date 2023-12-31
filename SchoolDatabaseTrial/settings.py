"""
Django settings for SchoolDatabaseTrial project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
# settings.py
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$u*05j6bvap3cq)m+odd=fpsr$n$tb7c@1in3@_qg$!ka%#poy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#ENVIRONMENT=os.environ.get('ENVIRONMENT', default='development')
ALLOWED_HOSTS = [".vercel.app"]
"""
#security settings
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
SECURE_SSL_REDIRECT=True
ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
    'mysite.com',
    '*'
]
"""
# ALLOWED_HOSTS = [
#     '192.168.43.216',
# ]

#security settings

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    #'Teacher.Teacher_views.Grade9_views.Grd9_teacher_models.Grade_9_Teacher_Class',
    #local apps
    'Student',
    'Teacher',
    'Headmin',
 "widget_tweaks",
    #Third party apps
    'crispy_forms',
    'chartit',
    'bootstrap4',
    'crispy_bootstrap4',  # Make sure this app is included
    # 'profile',
    'qa',
    'post',

    
    # # App
    'notification',
    # # App
    'review',
    # # App
    'tagbadge',
    
    # # App
    # 'help',
    'taggit',
'martor',
# 'simple_history',
    # 'background_task',
    'review.templatetags',
    'tagbadge.tb_templatetags',
    'online_users',
    'django_bootstrap5',
#     # 'debug_toolbar',
#     'tools',
]

MIDDLEWARE = [
    #'django.middleware.cache.UpdateCacheMiddleware',#new
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',#new
]
#caching database
"""
CACHE_MIDDLEWARE_ALIAS='default'
CACHE_MIDDLEWARE_SECONDS=604800
CACHE_MIDDLEWARE_KEY_PREFIX=''
"""
#caching database
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

ROOT_URLCONF = 'SchoolDatabaseTrial.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,os.path.join(BASE_DIR, 'template'), os.path.join(BASE_DIR, 'Headmin/template'), os.path.join(BASE_DIR, 'Teacher/template'),  os.path.join(BASE_DIR, 'Teacher/template/Grade9Teach/Tgrd9A'), os.path.join(BASE_DIR, 'Student/template/'),os.path.join(BASE_DIR, 'Teacher/template/Grade9Teach/Tgrd9B', os.path.join(BASE_DIR, 'Student/template/Grade9/Grd9ClsA'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'review.context_processors.reviewAnswer_cp',
                'review.context_processors.returnTrue',
                'review.context_processors.reviewQuestion_cp',
                'review.context_processors.returnTrue_or_False',
                'review.context_processors.reviewLateAnswer_cp',
                'review.context_processors.returnLateReview_True_or_False',
                'review.context_processors.reviewClosedQuestions',
                'review.context_processors.returnTrue_or_FalseClosedQuestions',
                'review.context_processors.reviewReOpenQuestion_sVotes',
                'review.context_processors.returnTrue_or_FalseUnCloseQuestion_s',
                'review.context_processors.reviewEditedPosts',
                'review.context_processors.returnTrue_or_FalseEditPosts',
                'review.context_processors.reviewLowQualityPosts',
                'review.context_processors.returnTrue_or_FalseLowPosts',
                'review.context_processors.reviewFlagPosts',
                'review.context_processors.returnTrue_or_FalseFlagPosts',
                'review.context_processors.reviewFlagComments',
                'review.context_processors.returnTrue_or_FalseFlagComments',
                'notification.context_processors.privNotificationViewer',
                'notification.context_processors.notificationViewer',
                'profile.context_processors.top_questions',
                'profile.context_processors.count_all_bounties',
            ],
        },
    },
]

WSGI_APPLICATION = 'SchoolDatabaseTrial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static')
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'






#login/logout redirect codes
AUTH_USER_MODEL='Headmin.Account'

LOGIN_URL='login'
LOGIN_REDIRECT_URL='profile_view'
LOGOUT_URL='logout'
LOGOUT_REDIRECT_URL='login'


INTERNAL_IPS = ['127.0.0.1', '0.0.0.0' ]

CRISPY_TEMPLATE_PACK='bootstrap4'
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'SchoolDatabaseTrial.settings')
application=get_wsgi_application()
app=application