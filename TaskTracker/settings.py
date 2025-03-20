from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r%a-%r8i5cg-#dmmfo*f5hzo9wvs#v4sb_m2v$0tvbxui3@^dj'


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'r-e-project.onrender.com',
    'task-tracker-bxwd.onrender.com',
    'task-tracker-mit4.onrender.com',
    '*.onrender.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://r-e-project.onrender.com',
    'https://task-tracker-bxwd.onrender.com',
    'https://task-tracker-mit4.onrender.com',
    'https://*.onrender.com',
]
DEBUG = True
# Security settings based on environment

# CSRF and session settings
CSRF_TRUSTED_ORIGINS = ['https://task-tracker-bxwd.onrender.com']
SECURE_SSL_REDIRECT = False  # Redirect HTTP to HTTPS
SESSION_COOKIE_SECURE = True  # Cookies over HTTPS only
CSRF_COOKIE_SECURE = True  # CSRF cookie over HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
    'crispy_forms',
    'crispy_bootstrap5',
]

# Crispy Forms settings (corrected typo)
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

AUTH_USER_MODEL = 'base.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TaskTracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'TaskTracker.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where collectstatic saves files
STATICFILES_DIRS = [BASE_DIR / 'static']  # Custom static directory

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

APPEND_SLASH = False  # Optional: Disable trailing slash redirect if not needed

# Debug output to verify settings
if DEBUG:
    print(f"DEBUG: {DEBUG}")
    print(f"SECURE_SSL_REDIRECT: {SECURE_SSL_REDIRECT}")

# filepath: [manage.py](http://_vscodecontentref_/9)
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaskTracker.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to create and  activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()