"""
Django settings for portfolio_project.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ----- Tiny .env loader (no extra dependency) -----
# Reads KEY=VALUE lines from a .env file at the project root and loads them
# into os.environ if they aren't already set. This lets you configure secrets
# (like the Gmail App Password) once instead of setting env vars each session.
_env_path = BASE_DIR / '.env'
if _env_path.exists():
    for _line in _env_path.read_text(encoding='utf-8').splitlines():
        _line = _line.strip()
        if not _line or _line.startswith('#') or '=' not in _line:
            continue
        _k, _v = _line.split('=', 1)
        _k = _k.strip()
        _v = _v.strip().strip('"').strip("'")
        os.environ.setdefault(_k, _v)

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-change-me-in-production-please-set-a-real-secret-key',
)

DEBUG = os.environ.get('DEBUG', 'True').lower() in ('1', 'true', 'yes', 'on')

# ALLOWED_HOSTS: comma-separated list via env. Render injects RENDER_EXTERNAL_HOSTNAME
# for the service's public URL — append it automatically so deploys "just work".
ALLOWED_HOSTS = [h.strip() for h in os.environ.get('ALLOWED_HOSTS', '*').split(',') if h.strip()]
_render_host = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if _render_host and _render_host not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(_render_host)

# CSRF trusted origins for the Render hostname (required when DEBUG=False).
CSRF_TRUSTED_ORIGINS = []
if _render_host:
    CSRF_TRUSTED_ORIGINS.append(f'https://{_render_host}')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise must come right after SecurityMiddleware so it can serve
    # /static/ files in production (Render runs DEBUG=False).
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_project.urls'

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

WSGI_APPLICATION = 'portfolio_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ----- Static files (CSS / JS / images) -----
# `portfolio/static/` is auto-discovered via AppDirsFinder (no STATICFILES_DIRS
# needed). STATIC_ROOT is where `collectstatic` writes the production bundle
# that WhiteNoise serves. Render's build step must run collectstatic.
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise: compressed + hashed filenames for long-term caching.
STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ===== Email Configuration =====
# Contact form messages are delivered to suryabhangirase777@gmail.com.
# Set EMAIL_HOST_USER and EMAIL_HOST_PASSWORD as environment variables
# (use a Gmail App Password, not your normal password).
# If credentials are not set, emails are printed to the console for development.
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

if EMAIL_HOST_USER and EMAIL_HOST_PASSWORD:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER or 'no-reply@portfolio.local'
CONTACT_RECIPIENT_EMAIL = 'suryabhangirase777@gmail.com'
