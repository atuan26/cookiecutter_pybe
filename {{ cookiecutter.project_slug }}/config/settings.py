import os
import environ
from pathlib import Path


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=['*'])

INSTALLED_APPS = [
{% if cookiecutter.admin_panel == 'django-grappelli' %}
    "grappelli",
{% elif cookiecutter.admin_panel == 'django-baton' %}
    "baton",
{% elif cookiecutter.admin_panel == 'django-simpleui' %}
    "simpleui",
{% elif cookiecutter.admin_panel == 'django-jazzmin' %}
    "jazzmin",
{% endif %}
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    #
{% if cookiecutter.admin_panel == 'django-baton' %}
    "baton.autodiscover",
{% endif %}
{% if cookiecutter.framework == 'Django + FastAPI' %}
    "apps.polls.apps.PollsConfig",
{% endif %}
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

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "config.wsgi.application"


import dj_database_url

DATABASES = {
    "default": dj_database_url.config(
        # conn_max_age=600,
    )
}
# DATABASES["default"].update({'OPTIONS': {'charset': 'utf8mb4'}})


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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
