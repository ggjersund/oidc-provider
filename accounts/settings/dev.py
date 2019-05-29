from . base import *


# SECURITY WARNING: CRITICAL SECURITY SETTINGS
# https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/#critical-settings

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'


# Email configuration
# https://docs.djangoproject.com/en/2.1/topics/email/#email-backends

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Static files (STATIC_URL is applied in the base.py settings file)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'var/static/')


# Media files (MEDIA_URL is applied in the base.py settings file)
# https://docs.djangoproject.com/en/2.1/topics/files/#managing-files

MEDIA_ROOT = os.path.join(BASE_DIR, 'var/media/')


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
