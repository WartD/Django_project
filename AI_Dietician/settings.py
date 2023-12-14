"""
Django settings для проекта AI_Dietician.

Сгенерировано с помощью 'django-admin startproject' с использованием Django 2.2.
Сейчас используется версия 5.0

Для дополнительной информации смотрите
https://docs.djangoproject.com/en/2.2/topics/settings/

Полный список настроек и их значений смотрите по адресу
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from pathlib import Path

# Строим пути внутри проекта, как это: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


# Настройки быстрого старта разработки - не предназначены для продакшена


# ВНИМАНИЕ К БЕЗОПАСНОСТИ: держите секретный ключ в продакшене в тайне!
SECRET_KEY = "sp_&-%fy-$&%e+)o$cm#eqerksdc3o+o1ho%pa%tzf==5ka62q"

# ВНИМАНИЕ К БЕЗОПАСНОСТИ: не используйте режим отладки в продакшене!
DEBUG = True

ALLOWED_HOSTS = ["*"]

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

STATIC_DIR = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Определение приложений

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home.apps.HomeConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "AI_Dietician.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "AI_Dietician.wsgi.application"


# База данных
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Проверка пароля
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Международизация
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Статические файлы (CSS, JavaScript, изображения)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "static/"

LOGIN_REDIRECT_URL = "/"    
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
