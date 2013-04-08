"""
Django settings for mmp project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
# Hardcoded values can leak through source control. Consider loading
# the secret key from an environment variable or a file instead.
SECRET_KEY = 'yfd1x8f07&cd(^)f9n@n@@6jpikqc_@jf1f4t*nvw#n=+wpg-o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party apps
    'south',
    'facebook_comments',

    # my apps
    'home',
    'people',
    'items',
    'actions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    #for facebook_comments to work
    'django.core.context_processors.request',

    # my context_processors
    # this one for including login form in every page
    "people.views.include_auth_forms",
)

ROOT_URLCONF = 'mmp.urls'

WSGI_APPLICATION = 'mmp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

HOST = ''

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mmp_local',
        'USER': 'postgres',
        'PASSWORD': '123',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

#templates directories
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    )

# static files directories
STATICFILES_DIRS = (
    ('base', os.path.join(BASE_DIR, 'bootstrap')),
    ('css', os.path.join(BASE_DIR, 'bootstrap/css')),
    ('js', os.path.join(BASE_DIR, 'bootstrap/js')),
    ('img', os.path.join(BASE_DIR, 'bootstrap/img')),
    ('less', os.path.join(BASE_DIR, 'bootstrap/less')),
    ('sm2', os.path.join(BASE_DIR, 'sm2')),
    )
# custom user model
AUTH_USER_MODEL = 'people.Person'

#media directory
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#media url
MEDIA_URL = '/media/'

LOGIN_URL = 'login_person'
LOGOUT_URL = 'front_page'
