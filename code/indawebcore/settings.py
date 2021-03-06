"""
Django settings for aincore project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import socket

DEPLOY_HOSTNAMES = [
    'anhel.in',
    'www.anhel.in',
]

DEPLOYED = socket.gethostname() in DEPLOY_HOSTNAMES

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't1mm_vl*qku+gokgm=))p@b6cp*5zdl6jeg@t_va62(x4+5g_q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = not DEPLOYED

ALLOWED_HOSTS = [
    'anhel.in',
    'www.anhel.in',
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markdown2',
    'sendfile',
    'files',
    'python_course_2.apps.PythonCourse2Config',
    'python_course.apps.PythonCourseConfig',
    'indaweb',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'indawebcore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'indawebcore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if DEPLOYED:
    from . import production_db_config
    DATABASES = production_db_config.DATABASES
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru_RU.utf8'

TIME_ZONE = 'Asia/Novosibirsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

if DEPLOYED:
    STATIC_URL = '//static.' + socket.gethostname() + "/"
    STATIC_ROOT = "/home/website/repo/static"
else:
    STATIC_URL = '/static/'

if DEPLOYED:
    STATICFILES_DIRS = []
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "../static"),
    ]

if DEPLOYED:
    MEDIA_ROOT = "/home/website/upload/"
    MEDIA_URL = "//static." + socket.gethostname() + "/upload/"
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, "upload")
    MEDIA_URL = "/media/"

UPLOADED_FILE_BASE_URL = MEDIA_URL + "files/"

if DEPLOYED:
    SENDFILE_BACKEND = 'sendfile.backends.nginx'
    SENDFILE_ROOT = MEDIA_ROOT
    SENDFILE_URL = '/upload/'
else:
    SENDFILE_BACKEND = 'sendfile.backends.development'

if DEPLOYED:
    SECURE_HSTS_SECONDS = 24 * 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_BROWSER_XSS_FILTER = True
