"""
Django settings for comong_project project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8ppqo!_58dymp&&w#g*xegy7pq!i31#zp22fo+dk2=2j2rp3h6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['comong-jennie-server.onrender.com','127.0.0.1','localhost', 'localhost:8000'] # 수정해야될수도
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    #-----------
    'rest_framework',
    'User',
    'Community',
    #-----------
    'allauth',
    'allauth.account',
    #'allauth.socialaccount',
    'corsheaders',

    
]

SITE_ID = 1 

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'User.middleware.ProfileSetupMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'comong_project.urls'

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

WSGI_APPLICATION = 'comong_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'comong_project',
#         'USER': 'jennie',
#         'PASSWORD': '1234',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
# # Replace this value with your local database's connection string.
#         default='postgresql://postgres:postgres@localhost:5432/comong_project',
#         conn_max_age=600

#Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    
    'default': dj_database_url.config (
        default='postgresql://hosung:nnaro9iGbquZ0LPsizwfRmB3quGIKS3D@dpg-cqjqhsaj1k6c73a1uc4g-a.singapore-postgres.render.com/comong',
        conn_max_age=600
    )
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "User.validators.CustomPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# This setting informs Django of the URI path from which your static files will be served to users
# Here, they well be accessible at your-domain.onrender.com/static/... or yourcustomdomain.com/static/...
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# This production code might break development mode, so we check whether we're in DEBUG mode
# if not DEBUG:
#     # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#     # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
#     # and renames the files with unique names for each version to support long-term caching
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Auth Settings

AUTH_USER_MODEL = "User.User"

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER':'User.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'User.backends.JWTAuthentication',
    ),
}

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_SIGNUP_REDIRECT_URL = "login"
LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_AUTHENTICATED_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_SIGNUP_FORM_CLASS = "User.forms.SignupForm"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_PASSWORD_IUPUT_RENDER_VALUE = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "account_email_confirmation_done"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_email_confirmation_done"
PASSWORD_RESET_TIMEOUT_DAYS = 3

# Email settings

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"