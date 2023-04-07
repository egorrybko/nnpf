"""
Django settings for image_pnev project.
Generated by 'django-admin startproject' using Django 4.0.6.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9sb$-*w&x4zup&$p)#@r7$1rm)jtnd#_kxqhu!u+$m^74p%s&x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'thumbnailer.apps.ThumbnailerConfig',
    'widget_tweaks',
    'django.contrib.sites',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'image_pnev.urls'

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
                'account.context_processors.account',
            ],
        },
    },
]

WSGI_APPLICATION = 'image_pnev.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CSRF_TRUSTED_ORIGINS = ['https://egorrybko-stunning-space-enigma-9gpg7jjwgqv2xrxp-8000.preview.app.github.dev','https://127.0.0.1']

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

ACCOUNT_LANGUAGES = ("en", "English"), ("ru", "Русский")
ACCOUNT_TIMEZONES = ("Europe/Moscow", 'Москва +3'), ('UTC', 'UTC')
SITE_ID = 2

ACCOUNT_LOGIN_URL = 'yourapp:account_login'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = ACCOUNT_LOGIN_URL
ACCOUNT_PASSWORD_RESET_REDIRECT_URL = ACCOUNT_LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_URL = "yourapp:account_confirm_email"
ACCOUNT_SETTINGS_REDIRECT_URL = 'yourapp:account_settings'
ACCOUNT_PASSWORD_CHANGE_REDIRECT_URL = "yourapp:account_password"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# celery
#CELERY_BROKER_URL = 'redis://redis:6379/0'
#CELERY_RESULT_BACKEND = "redis"
#CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
#CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379")
#CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "redis://redis:6379")
CELERY_BROKER_URL = 'redis://redis:6379'
#CELERY_RESULT_BACKEND = "redis"
CELERY_RESULT_BACKEND = 'redis://redis:6379'
#redis://localhost:6379
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))
IMAGES_DIR = os.path.join(MEDIA_ROOT, 'images')
if not os.path.exists(MEDIA_ROOT) or not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)