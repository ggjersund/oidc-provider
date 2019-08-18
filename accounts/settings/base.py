import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'wtuxxa(p24&6d9)g*wyd(^ci)53!ys!bl!h9up((t*)lohyhgk'


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('nb', 'norsk (bokmål)'),
    ('en', 'English'),
]

LOCALE_PATHS = [os.path.join(BASE_DIR, 'shared/locale'),]

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'shared/static'),]


# Media files (MEDIA_ROOT is applied in state settings)
# https://docs.djangoproject.com/en/2.1/topics/files/#managing-files

MEDIA_URL = '/media/'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # External dependencies
    'user_sessions',
    'oidc_provider',
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
    # Internal dependencies
    'apps.account',
    'apps.users',
    'apps.authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'apps.users.middleware.TempFixUserSessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'accounts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'shared/templates')
        ],
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

WSGI_APPLICATION = 'accounts.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Django user sessions
# https://django-user-sessions.readthedocs.io/en/stable/installation.html#installation

SESSION_ENGINE = 'user_sessions.backends.db'


# Custom user model
# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#substituting-a-custom-user-model

AUTH_USER_MODEL = 'users.User'


# Login settings
# https://docs.djangoproject.com/en/2.2/ref/settings/#login-url

LOGIN_URL = 'two_factor:login'

LOGIN_REDIRECT_URL = 'account:index'

LOGOUT_REDIRECT_URL = 'two_factor:login'


# Geo-location data
# https://docs.djangoproject.com/en/2.2/ref/contrib/gis/geoip2/

GEOIP_PATH = os.path.join(BASE_DIR, 'shared/static/geodata')
