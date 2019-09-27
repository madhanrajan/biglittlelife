"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# Runserver command "python manage.py runserver_plus --cert-file /tmp/cert"


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'blog', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'blog', 'static')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_-==mx5#x8hrm!&t-awnz-k)=+yjb221k#uryz4ae$bx@)7yze'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['biglittle.life', 'www.biglittle.life', '68.183.154.129']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Extra django stuff
    'django.contrib.sites',

    # Installed 3rd party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'django_extensions',
    'profanity_check',
    'crispy_forms',
    'bootstrap_pagination',
    'rest_framework',
    'dateparser',


    # Custom django apps
    'blog',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }
# else:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite',
        'USER': 'madhan',
        'PASSWORD': 'stayreal357',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    STATIC_DIR,
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    'allauth.account.auth_backends.AuthenticationBackend',

]

SITE_ID = 1

LOGIN_REDIRECT_URL = 'post_list'

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

POSTMAN_DISALLOW_ANONYMOUS = True

POSTMAN_DISALLOW_MULTIRECIPIENTS = True

POSTMAN_DISALLOW_COPIES_ON_REPLY = True

POSTMAN_AUTOCOMPLETER_APP = {
    'name': 'ajax_select',  # default is 'ajax_select'
    'field': 'AutoCompleteField',  # default is 'AutoCompleteField'
    'arg_name': 'channel',  # default is 'channel'
    'arg_default': 'postman_friends',  # no default, mandatory to enable the feature
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
     {'METHOD': 'oauth2',
      'SCOPE': ['email', 'public_profile', 'user_friends'],
      'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
      'FIELDS': [
          'id',
          'email',
          'name',
          'first_name',
          'last_name',
          'verified',
          'locale',
          'timezone',
          'link',
          'gender',
          'updated_time'],
      'EXCHANGE_TOKEN': True,
      'LOCALE_FUNC': lambda request: 'kr_KR',
      'VERIFIED_EMAIL': False,
      'VERSION': 'v2.4'}}
